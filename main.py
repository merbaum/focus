#! /usr/bin/python3.6
#
# Reference used:
# https://www.devdungeon.com/content/desktop-notifications-linux-python
#
#
# This one is required, but should already be installed
# sudo apt-get install python-gobject
#
# Installing this will install the
# notify-send program. Check that out
# for sending notifications in the shell
# sudo apt-get install libnotify-bin
#
# The development headers if you
# want to do any development in C/C++
# sudo apt-get install libnotify-dev

import sys
import time

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

class Focus():
    notification = 0

    # default repeat is 4 times(2 hours)
    # default focus time is 25 minutes
    # default relax time is 5 minutes
    def __init__(self, repeat: int = 4, focus_timer: int = 1500, relax_timer: int = 300):
        if len(sys.argv) > 1:
            repeat = int(sys.argv[1])
            # print (str(repeat))

        if len(sys.argv) > 2:
            focus_timer = int(sys.argv[2])
            # print (str(focus_timer))

        if len(sys.argv) > 3:
            relax_timer = int(sys.argv[3])
            # print (str(relax_timer))

        self.repeat = repeat
        self.focus_timer = focus_timer
        self.relax_timer = relax_timer

        Notify.init("Focus")
        self.focussing()


    def focussing(self):
        repeat = self.repeat
        focus_timer = self.focus_timer
        relax_timer = self.relax_timer

        self.create_notification()
        while repeat > 0:
            repeat -= 1

            self.update_notification('Focus!', 'Everyone be quiet please!')
            # print ('Focus!')
            self.show_notification()
            time.sleep(focus_timer)

            self.update_notification('Relax!', 'Yay!')
            # print ('Relax!')
            self.show_notification()
            time.sleep(relax_timer)

        self.update_notification('Done!', 'Have a nice day!')
        # print ('Done!')
        self.show_notification()

        self.cleanup()



    def create_notification(self, subject = 'Hello', body = 'Hello, world!'):
        self.notification = Notify.Notification.new(subject, body)

    def update_notification(self, subject = 'Hello', body = 'Hello, world!'):
        self.notification.update(subject, body)

    def show_notification(self):
        self.notification.show()

    def cleanup(self):
        Notify.uninit()

Focus()

#!/usr/bin/python
import os
import pynotify
'''
    This scripts changes the keyboard layout, its recommendable that assign it to a keyboard shortcut.
'''


def notify(new_layout):
    pynotify.init("Keyboard")
    notice = pynotify.Notification("Set Keyboard Layout" + str(new_layout))
    notice.show()

CURRENT_LAYOUT_COMMAND = "setxkbmap -query | grep layout"
current_layout = os.popen(CURRENT_LAYOUT_COMMAND, 'r', 1)
layout_temp_list = []

for line in current_layout:
    layout_temp_list.append(line)
layout = layout_temp_list[0].split(":")

if str(layout[1]).__contains__("us"):
    os.system("setxkbmap latam")
    notify(layout[1])

elif str(layout[1]).__contains__("latam"):
    os.system("setxkbmap us")
    notify(layout[1])

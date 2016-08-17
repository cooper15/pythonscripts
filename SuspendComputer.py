#!/usr/bin/python
from time import sleep
import os
import pynotify
import logging
# Constant definitions needs Upower
BATTERY_STATUS_COMMAND = 'upower -i $(upower -e | grep BAT) ' \
                         '| grep --color=never -E "state|to\ full|to\ empty|percentage"'
SUSPEND_COMMAND = "systemctl suspend"
MINIMUM_PERCENTAGE = '17%'


def get_battery_status():
    battery_status_file = os.popen(BATTERY_STATUS_COMMAND, 'r', 1)
    array_file = []
    for line in battery_status_file:
        array_file.append(line)

    # Status can be: charging, discharging or fully-charged
    status = array_file[0]
    status = status.split(":")
    status = status[1].strip()
    # Battery percentage: from 15 % to 100 %
    if "fully-charged" == status:
        percentage = array_file[1]
    else:
        percentage = array_file[2]
    percentage = percentage.split(":")
    percentage = percentage[1]
    percentage = percentage.strip()
    array_file = [status, percentage]
    return array_file


def notification(message_type):
    if 1 == message_type:
        message = "The system will be suspend in 10 seconds."
    elif 2 == message_type:
        message = "Starting Battery status Script."

    pynotify.init("Attention")
    notice = pynotify.Notification("Attention!", message)
    notice.show()


def principal_loop():
    logging.basicConfig(
        format='%(asctime)s %(message)s', filename="/home/cooper15/.scripts/suspend_status.log", level=logging.DEBUG)
    logging.debug("starting")
    notification(2)
    while True:
        battery_status = get_battery_status()
        print battery_status[0]
        if "discharging" == battery_status[0] and battery_status[1] < MINIMUM_PERCENTAGE:
            notification(1)
            sleep(10)
            logging.debug("Suspending battery percentage " + battery_status[1])
            os.system(SUSPEND_COMMAND)
        elif "discharging" == battery_status[0] and battery_status[1] > MINIMUM_PERCENTAGE:
            logging.debug("Sleeping script +60 seconds" + battery_status[1])
            sleep(30)
        elif "charging" == battery_status[0] or "fully-charged" == battery_status[0]:
            logging.debug(battery_status[0] + battery_status [1])
            sleep(5)

if __name__ == '__main__':
    principal_loop()

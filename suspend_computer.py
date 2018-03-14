"""This simple script will suspend the computer
    if the battery get to a critic level"""

import subprocess
import logging
from os import system
from time import sleep
import re

MINIMUM_LEVEL_ALLOWED = 0.17
NUMERIC_LEVEL = "(?<=, )[0-9].*(?=%)"
STATUS = "(?<=: ).*[a-z](?=,)"
SUSPEND_COMPUTER = "systemctl suspend -i"


class Suspend(object):
    args = ["acpi"]

    def get_battery_status(self):
        process = subprocess.Popen(self.args, stdout=subprocess.PIPE, shell=True)
        output = str(process.communicate()[0])
        return output

    def is_battery_under_minimum_allowed(self):
        level = int(re.search(NUMERIC_LEVEL, self.get_battery_status()).group(0)) / 100
        return level < MINIMUM_LEVEL_ALLOWED

    def is_status_discharging(self):
        status = re.search(STATUS, self.get_battery_status()).group(0)
        return status == "Discharging"

    def is_battery_under_minimum_level_allowed_and_discharging(self):
        return self.is_battery_under_minimum_allowed() and self.is_status_discharging()

    def infinite_loop(self):
        while True:
            if self.is_battery_under_minimum_level_allowed_and_discharging():
                system(SUSPEND_COMPUTER)
            else:
                sleep(5)


if __name__ == '__main__':
    suspend_pc = Suspend()
    suspend_pc.infinite_loop()

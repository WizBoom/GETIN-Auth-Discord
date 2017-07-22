from threading import Thread
from time import sleep

import schedule


class Scheduler(Thread):

    def __init__(self, util, NEW_APPS_SLEEP_TIME, SYNC_SLEEP_TIME, KILLBOARD_SLEEP_TIME):
        self.util = util
        self.NEW_APPS_SLEEP_TIME = NEW_APPS_SLEEP_TIME
        self.SYNC_SLEEP_TIME = SYNC_SLEEP_TIME
        self.KILLBOARD_SLEEP_TIME = KILLBOARD_SLEEP_TIME

    def setup(self):
        schedule.every(self.NEW_APPS_SLEEP_TIME).seconds().do(self.check_apps)
        schedule.every(self.SYNC_SLEEP_TIME).seconds().do(self.sync)
        schedule.every(self.KILLBOARD_SLEEP_TIME).seconds().do(self.killboard)

    def check_apps(self):
        self.util.bot.send_message(self.util.config['PRIVATE_COMMAND_CHANNELS']['RECRUITMENT'], self.util.check_apps())

    def sync(self):
        self.util.bot.send_message(self.util.config['PRIVATE_COMMAND_CHANNELS']['RECRUITMENT'], self.util.sync())

    def killboard(self):
        self.util.bot.send_message(self.util.config['PRIVATE_COMMAND_CHANNELS']['RECRUITMENT'], self.util.check_killboard())

    def run(self):
        while True:
            schedule.run_pending()
            sleep(1)

import logging
import sys
import time

import schedule
from django.core.management.base import BaseCommand

from interview_checker.bot import GlobalEntryBot

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s |%(message)s')


class Command(BaseCommand):
    help = 'Runs the bot'

    def handle(self, *args, **options):
        bot = GlobalEntryBot()
        bot.send_updates(dry_run=True)
        schedule.every(5).minutes.do(bot.send_updates, None, False)
        logging.info(schedule.jobs)
        while True:
            schedule.run_pending()
            time.sleep(1)
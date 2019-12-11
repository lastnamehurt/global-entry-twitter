import logging
import os
import sys
import time

import tweepy
import schedule

from interview_checker.servcies import convert_datetime_to_string, interview_finder_service

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s |%(message)s')


class Auth:
    CONSUMER_KEY = os.environ.get('GLOBAL_ENTRY_CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('GLOBAL_ENTRY_CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('GLOBAL_ENTRY_ACCESS_TOKEN')
    TOKEN_SECRET = os.environ.get('GLOBAL_ENTRY_TOKEN_SECRET')


class GlobalEntryBot(object):

    def __init__(self):
        self.auth = tweepy.OAuthHandler(Auth.CONSUMER_KEY, Auth.CONSUMER_SECRET)
        self.auth.set_access_token(Auth.ACCESS_TOKEN, Auth.TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    @classmethod
    def parse_object_for_tweet(cls, instance):
        date = instance.appointment_date
        location = instance.location_name
        new_date = convert_datetime_to_string(date)
        # NOTE: reset date_changed flag here
        instance.date_changed = False
        return "Global Entry appointment available in {} on {}".format(location, new_date)

    def get_updates(self):
        updates = []
        slots = interview_finder_service.repo.list_all()
        for slot in slots:
            logging.info("Looking at {}".format(slot.location_name))
            interview_finder_service.get_new_appointment(slot.location_id)
        updates.extend(list(interview_finder_service.repo.filter(date_changed=True)))
        return updates

    def send_updates(self, updates=None, dry_run=True):
        if not updates:
            updates = self.get_updates()
        for update in updates:
            tweet = self.parse_object_for_tweet(update)
            if dry_run:
                logging.info("Would Tweet: {}".format(tweet))
                print("Would Tweet: {}".format(tweet))
            else:
                try:
                    self.api.update_status(tweet)
                    time.sleep(2)
                except:
                    pass

    # def run(self, interval=5):
    #     self.send_updates(dry_run=False)
    #     schedule.every(interval).minutes.do(self.send_updates, None, False)
    #     while True:
    #         try:
    #             logging.info(schedule.jobs)
    #             schedule.run_pending()
    #             time.sleep(1)
    #         except:
    #             sys.exit()
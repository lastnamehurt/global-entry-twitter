import logging
import time

from interview_checker.bot import GlobalEntryBot
from interview_checker.constants import LOCATIONS_MAP
from interview_checker.repos import interview_slot_repo
from interview_checker.servcies import interview_finder_service

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s |%(message)s')


def backfill_global_entry_interview_timeslots():
    backfills = []
    for location, data in LOCATIONS_MAP.iteritems():
        logging.info("Backfilling {} with id <{}>".format(location, data['id']))
        obj = interview_slot_repo.create(location_name=data['name'], location_id=data['id'])
        # grab date
        appointment_date = interview_finder_service._get_new_appointment_datetime(data['id'])
        # save to db
        obj.appointment_date = appointment_date
        obj.save()

        backfills.append(obj)

    return backfills


def post_initial_appointments(dry=True):
    bot = GlobalEntryBot()
    for backfill in list(interview_slot_repo.filter(appointment_date__isnull=False)):
        tweet = GlobalEntryBot.parse_object_for_tweet(backfill)
        if dry:
            print(tweet)
        else:
            bot.api.update_status(tweet)
            time.sleep(5)

def backfill_single_model(location_id):
    for val in LOCATIONS_MAP.values():
        if val['id'] == location_id:
            obj = interview_slot_repo.create(location_name=val['name'], location_id=location_id)
            appointment_date = interview_finder_service._get_new_appointment_datetime(val['id'])
            # save to db
            obj.appointment_date = appointment_date
            obj.save()
    return obj
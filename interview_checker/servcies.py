import datetime
import json
import logging

import requests

from interview_checker.constants import Constants
from interview_checker.repos import InterviewSlotRepo

convert_timestamp_to_datetime_string = lambda timestamp: ' '.join(timestamp.split("T"))
convert_datetime_string_to_datetime = lambda timestamp_string: datetime.datetime.strptime(timestamp_string,
                                                                                          "%A, %b. %d %H:%M")
convert_to_datetime_from_string_with_dashes = lambda timestamp_string: datetime.datetime.strptime(timestamp_string,
                                                                                                  "%Y-%m-%d %H:%M")
convert_datetime_to_string = lambda date_time: datetime.datetime.strftime(date_time, "%A, %b. %d, %Y @ %H:%M")
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s |%(message)s')


class InterviewFinderService:
    repo = InterviewSlotRepo()

    def is_new_appointment_date(self, location_id, date):

        if not date:
            return False

        location = self.repo.get(location_id=location_id)

        if not location.appointment_date:
            location.appointment_date = date
            location.date_changed = True
            location.save()
            return True

        if location.appointment_date.date() != date.date():
            location.appointment_date = date
            location.date_changed = True
            location.save()
            return True
        location.date_changed = False
        location.save()
        return False

    def _get_new_appointment_datetime(self, location_id):
        logging.info("Fetching appointment for <{}>".format(location_id))

        appointment_request = requests.get(Constants.SCHEDULER_API_ENDPOINT.format(location_id))
        appointment = json.loads(appointment_request.text)

        if not appointment:
            return

        start_timestamp = appointment[0]['startTimestamp']
        start_time_string = convert_timestamp_to_datetime_string(start_timestamp)
        start_datetime = convert_to_datetime_from_string_with_dashes(start_time_string)

        # save to db
        # location = self.repo.get(location_id=location_id)
        # location.appointment_date = start_datetime
        # location.save()

        return start_datetime

    def get_new_appointment(self, location_id):
        # get startTimestamp
        start_datetime = self._get_new_appointment_datetime(location_id)
        if self.is_new_appointment_date(location_id, start_datetime):
            return start_datetime

    def sync_appointment_date(self, location_id, date):
        location = self.repo.get(location_id=location_id)
        if self.is_new_appointment_date(location_id, date):
            location.appointment_date = date
            location.save()
            logging.info("Saved new date to {}".format(location.location_name))
            return True


interview_finder_service = InterviewFinderService()

import logging

logger = logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s |%(message)s')


class Constants:

    JFK_ID = 5140
    DENVER_ID = 6940
    BOSTON_ID = 5441
    MEMPHIS = 13621
    DC_ID = 5142
    PORTLAND_ID = 7960
    DALLAS_ID = 5300
    PITTSBURGH_ID = 9200
    LOCATION_ID = None
    SCHEDULE_INTERVIEW_LINK = 'https://ttp.cbp.dhs.gov/schedulerapi/locations/{}/slots?startTimestamp={}T00%3A00%3A00&endTimestamp=''T00%3A00%3A00'.format(
        LOCATION_ID, '', '')
    SCHEDULER_API_ENDPOINT = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={}&minimum=1'
    ALL_LOCATIONS_DATA_ENDPOINT = 'https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true'


# example response
# u'[ {\n  "locationId" : 6940,\n  "startTimestamp" : "2020-09-02T10:15",
# \n  "endTimestamp" : "2020-09-02T10:30",\n  "active" : true,\n  "duration" : 15\n} ]'
LOCATIONS_MAP = {
    'JFK': {'id': Constants.JFK_ID, 'name': 'JFK'},
    'Denver': {'id': Constants.DENVER_ID, 'name': 'Denver'},
    'Boston': {'id': Constants.BOSTON_ID, 'name': 'Boston'},
    'Dulles': {'id': Constants.DC_ID, 'name': 'Dulles'},
    'Portland': {'id': Constants.PORTLAND_ID, 'name': 'Portland'},
    'Dallas': {'id': Constants.DALLAS_ID, 'name': 'DFW'},
    'Philadelphia': {'id': Constants.PITTSBURGH_ID, 'name': 'Pittsburgh'},
}

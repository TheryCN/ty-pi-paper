from __future__ import print_function
import httplib2
try:
    from urllib.parse import urlencode
except ImportError:
     from urllib import urlencode

import json
import time
import sys
import datetime

class CalendarService:
    """ Calendar Service used to query google calendar API.
    """

    access_token = ""

    def __init__(self , access_token):
        self.credentials = {}
        self.access_token = access_token

    def get_events(self, get_events_uri):
        http_obj = httplib2.Http()
        headers = {'Authorization': "Bearer " + self.access_token}
        now = datetime.datetime.utcnow()
        nowPlusOneDay = now + datetime.timedelta(days=1)
        timeMin = now.isoformat("T") + "Z"
        timeMax = nowPlusOneDay.isoformat("T") + "Z"
        resp, content = http_obj.request(uri=get_events_uri + "?timeMin=" + timeMin + "&timeMax=" + timeMax, method='GET', headers=headers)

        return json.loads(content)

from __future__ import print_function
from authentication import LimitedInputDeviceAuth
from gcalendar import CalendarService

import json

if __name__ == '__main__':
    # Gets the token
    config = {}
    with open("resources/config.json") as config_file:
        config = json.load(config_file)

    auth = LimitedInputDeviceAuth(config)

    access_token = auth.access_token
    if auth.access_token == "":
        auth.auth_verification_url()
        auth.auth()
        access_token = auth.access_token

    event_response = CalendarService(access_token).get_events(config["getEvents"])
    for item in event_response["items"]:
        print(item["summary"])

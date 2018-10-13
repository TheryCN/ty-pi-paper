from __future__ import print_function
from inkwriter import InkWriter
from PIL import ImageFont

import json
import time
import sys
import datetime
import os

class CalendarWriter(InkWriter):
    """ Calendar E-INK Writer.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = dir_path + "/resources/config.json"

    def write(self, epd, frame_black, frame_red):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20)

        # Load configuration
        config = {}
        with open(config_path) as config_file:
            config = json.load(config_file)

        auth = LimitedInputDeviceAuth(config)

        access_token = auth.access_token
        if auth.access_token == "":
            verification_url = auth.auth_verification_url()
            # Display Google validation URL
            epd.draw_string_at(frame_black, 4, 30, verification_url, font, InkWriter.COLORED)
            auth.auth()
        else:
            event_response = CalendarService(access_token).get_events(config["getEvents"])
            # Display events
            texts = []
            for item in event_response["items"]:
                texts.append(item["start"]["date"]  + " - " + item["summary"])

            epd.draw_strings_reverse_at(frame_black, 5, 5, texts, font, InkWriter.COLORED)

from inkwriter import InkWriter
from httplib2 import Http

import json
import os
from PIL import ImageFont

class CountdownWriter(InkWriter):

    config = {}

    def __init__(self, config):
        self.config = config

    def write(self, epd, frame_black, frame_highlight):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 25)

        http_obj = Http()
        resp, content = http_obj.request(uri=self.config.get_countdown_uri(), method='GET')
        content = json.loads(content.decode());

        # Write event type
        epd.draw_string_horizontal_at(frame_black, 10, 10, "{0}".format(content["type"]), font, InkWriter.COLORED)

        # Write event name
        epd.draw_string_horizontal_at(frame_highlight, 10, 30, "{0}".format(content["name"]), font, InkWriter.COLORED)

        # Write days
        epd.draw_string_horizontal_at(frame_black, 10, 50, "{0} DAYS".format(content["days"]), font, InkWriter.COLORED)

        # Write seconds
        epd.draw_string_horizontal_at(frame_highlight, 10, 70, "{0} SECONDS".format(content["seconds"]), font, InkWriter.COLORED)

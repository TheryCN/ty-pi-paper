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
        resp, content = http_obj.request(uri=self.config.get_countdown(), method='GET')
        content = json.loads(content.decode());

        # Write event type in red
        epd.draw_string_horizontal_at(frame_highlight, 10, 10, "{0}".format(content["type"]), font, InkWriter.COLORED)

        # Write days in black
        epd.draw_string_horizontal_at(frame_black, 10, 30, "{0} DAYS".format(content["days"]), font, InkWriter.COLORED)

        # Write hours in red
        epd.draw_string_horizontal_at(frame_highlight, 10, 50, "{0} SECONDS".format(content["seconds"]), font, InkWriter.COLORED)

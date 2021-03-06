from inkwriter import InkWriter
from httplib2 import Http

import json
import os
from PIL import ImageFont

class CountdownWriter(InkWriter):

    config = {}
    fontName = '/usr/share/fonts/truetype/freefont/FreeMono.ttf';

    def __init__(self, config):
        self.config = config

    def write(self, epd, frame_black, frame_highlight):
        font = ImageFont.truetype(self.fontName, 25)

        http_obj = Http()
        resp, content = http_obj.request(uri=self.config.get_countdown_uri(), method='GET')
        content = json.loads(content.decode());

        # Write event type
        epd.draw_string_horizontal_at(frame_black, 10, 10, "{0}".format(content["type"]), font, InkWriter.COLORED)

        # Write event name
        nameFontSize = 25
        name = content["name"]
        y = 35
        if len(name) > 15:
            nameFontSize = 15
            y = 40
            if len(name) > 25:
                name = name[:25] + "..."
        fontForName = ImageFont.truetype(self.fontName, nameFontSize);
        epd.draw_string_horizontal_at(frame_highlight, 10, y, "{0}".format(name), fontForName, InkWriter.COLORED)

        # Write days
        epd.draw_string_horizontal_at(frame_black, 10, 60, "{0} DAYS".format(content["days"]), font, InkWriter.COLORED)

        # Write seconds
        epd.draw_string_horizontal_at(frame_highlight, 10, 85, "{0} SECONDS".format(content["seconds"]), font, InkWriter.COLORED)

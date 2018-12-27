from __future__ import print_function
from inkwriter import InkWriter
from httplib2 import Http

import json
from PIL import ImageFont

class RandomCountdown(InkWriter):
    """ RandomCountdown E-INK Writer.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    countdown_path = dir_path + "/resources/config.json"

    def __init__(self):
        self.config = config
        with open(self.countdown_path) as file:
            self.config = json.load(file)

    def write(self, epd, frame_black, frame_red):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 25)

        http_obj = Http()
        resp, content = http_obj.request(uri=self.config["uri"], method='GET')
        content = json.loads(content);

        # Write event type in red
        epd.draw_string_reverse_at(frame_red, 10, 10, "{0}".format(content["event"]), font, InkWriter.COLORED)

        # Write days in black
        epd.draw_string_reverse_at(frame_black, 10, 30, "{0} DAYS".format(content["days"]), font, InkWriter.COLORED)

        # Write hours in red
        epd.draw_string_reverse_at(frame_red, 10, 50, "{0} SECONDS".format(content["seconds"]), font, InkWriter.COLORED)

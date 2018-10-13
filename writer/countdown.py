from __future__ import print_function
from inkwriter import InkWriter

import datetime
from PIL import ImageFont

class BirthdayWriter(InkWriter):
    """ Birthday countdown E-INK Writer.
    """

    def __init__(self):
        self.now = datetime.datetime.now()
        # Compute next birthday date
        self.birthday = datetime.datetime(self.now.year, 11, 4)

    def write(self, epd, frame_black, frame_red):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 25)
        delta = self.birthday - self.now

        # Write days in black
        epd.draw_string_reverse_at(frame_black, 10, 10, "{0} DAYS".format(delta.days), font, InkWriter.COLORED)

        # Write seconds in red
        epd.draw_string_reverse_at(frame_red, 10, 30, "{0} SECONDS".format(delta.seconds), font, InkWriter.COLORED)

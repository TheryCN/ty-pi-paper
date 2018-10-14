from __future__ import print_function

import epd2in13b
import sched, time

from PIL import Image, ImageFont, ImageDraw

from urllib.parse import urlparse
from writer.gcalendar import CalendarWriter
from writer.countdown import BirthdayWriter

def main():
    epd = epd2in13b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * int(epd.width * epd.height / 8)
    frame_red = [0xFF] * int(epd.width * epd.height / 8)

    # display images
    # frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
    # frame_red = epd.get_frame_buffer(Image.open('red.bmp'))
    # epd.display_frame(frame_black, frame_red)

    BirthdayWriter().write(epd, frame_black, frame_red)
    epd.display_frame(frame_black, frame_red)

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, actionargs))
    action(*actionargs)

if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    # Refresh every minutes
    periodic(scheduler, 60, main)

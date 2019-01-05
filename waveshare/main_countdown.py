# 2.9inch e-paper display (C) Countdown.

import epd2in9b
from PIL import Image, ImageFont, ImageDraw
import sched, time
import traceback

from countdown.config import Config
from countdown.writer import CountdownWriter

config = Config();
writer = CountdownWriter(config);

def main():
    try:
        epd = epd2in9b.EPD()
        epd.init()

        print("Clear frames")
        # Clear the frame buffer - There is no partial refresh
        frame_black = [0xFF] * int(epd.width * epd.height / 8)
        frame_highlight = [0xFF] * int(epd.width * epd.height / 8)

        # Draw chrono image

        print("Drawing Countdown")
        writer.write(epd, frame_black, frame_highlight)

        # Draw meteo (?)

        # display the frames
        epd.display_frame(frame_black, frame_highlight)
    except:
        print('traceback.format_exc():\n%s',traceback.format_exc())
        exit()

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, actionargs))
    action(*actionargs)

if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    # Refresh every hours
    periodic(scheduler, 60 * 60, main)
    scheduler.run()

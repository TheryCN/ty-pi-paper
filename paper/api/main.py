# 2.9inch e-paper display (C) Display from manager.

from waveshare import epd2in9b
from PIL import Image, ImageFont, ImageDraw
import sched, time
import traceback
import json
import os

from writer_factory import WriterFactory

writerFactory = WriterFactory()

def main(globalConfig):
    try:
        # Init edp
        epd = epd2in9b.EPD()
        epd.init()

        print("Clear frames")
        # Clear the frame buffer - There is no partial refresh
        frame_black = [0xFF] * int(epd.width * epd.height / 8)
        frame_highlight = [0xFF] * int(epd.width * epd.height / 8)

        # Draw image
        if 'active' in globalConfig.keys():
            active = globalConfig['active'];
            print("Drawing " + active)
            writerFactory.get_writer(active).write(epd, frame_black, frame_highlight)
        else:
            print("Drawing default")
            writerFactory.get_writer('image').write(epd, frame_black, frame_highlight)

        # Display the frames
        epd.display_frame(frame_black, frame_highlight)
        epd.sleep()
    except:
        print('traceback.format_exc():\n%s',traceback.format_exc())
        exit()

def periodic(scheduler, interval, action, actionargs={}):
    # Read global config
    globalConfig = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/../config.json') as file:
        globalConfig = json.load(file)

    if 'refreshTime' in globalConfig.keys():
        interval = globalConfig['refreshTime']

    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, globalConfig))
    action(globalConfig)

if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    # Refresh every 2 minutes
    periodic(scheduler, 60 * 2, main)
    scheduler.run()

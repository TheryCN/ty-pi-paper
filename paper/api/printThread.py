from threading import Thread
#from flask import current_app
import traceback
from waveshare import epd2in9b
from PIL import Image, ImageFont, ImageDraw
from writer_factory import WriterFactory
import sched, time

class PrintThread(Thread):

    def __init__(self, active, refreshTime):
        Thread.__init__(self)
        self.settings(active, refreshTime)
        self.writerFactory = WriterFactory()
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def settings(self, active, refreshTime):
        self.active = active
        self.refreshTime = 60

    def run(self):
        self.running = True
        periodic(scheduler, self.refreshTime, self.print_paper)
        scheduler.run()

    def stop(self):
        self.running = False
        self.scheduler.cancel(self.event)

    def print_paper(self):
        #current_app.logger.info('PrintThread#Print')
        try:
            # Init edp
            epd = epd2in9b.EPD()
            epd.init()

            print("Clear frames")
            # Clear the frame buffer - There is no partial refresh
            frame_black = [0xFF] * int(epd.width * epd.height / 8)
            frame_highlight = [0xFF] * int(epd.width * epd.height / 8)

            # Draw image
            print("Drawing " + self.active)
            self.writerFactory.get_writer(self.active).write(epd, frame_black, frame_highlight)

            # Display the frames
            epd.display_frame(frame_black, frame_highlight)
            epd.sleep()
        except:
            print('traceback.format_exc():\n%s',traceback.format_exc())
            exit()

def periodic(scheduler, interval, action, actionargs={}):
    if self.running:
        self.event = scheduler.enter(interval, 1, periodic,
                        (scheduler, interval, action, actionargs))
        action(actionargs)

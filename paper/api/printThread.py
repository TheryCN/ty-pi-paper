from threading import Thread
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
        self.refreshTime = refreshTime

    def run(self):
        self.running = True
        self.periodic()
        self.scheduler.run()

    def stop(self):
        self.running = False
        while not self.ends:
            time.sleep(2)
        self.scheduler.cancel(self.event)

    def print_paper(self):
        try:
            self.ends = False
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
            self.ends = True
        except:
            print('traceback.format_exc():\n%s',traceback.format_exc())
            self.ends = True

    def periodic(self):
        if self.running:
            self.event = self.scheduler.enter(self.refreshTime, 1, self.periodic)
            self.print_paper()

from threading import Thread
#from flask import current_app
import traceback
from waveshare import epd2in9b
from PIL import Image, ImageFont, ImageDraw
from waveshare.writer_factory import WriterFactory

class PrintThread(Thread):

    def __init__(self, active):
        Thread.__init__(self)
        self.active = active
        self.writerFactory = WriterFactory()

    def run(self):
        self.print_paper()

    def stop(self):
        self.running = False

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

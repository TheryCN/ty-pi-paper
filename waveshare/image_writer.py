from inkwriter import InkWriter
from httplib2 import Http

from PIL import Image

class ImageWriter(InkWriter):

    def write(self, epd, frame_black, frame_highlight):
        frame_black[:] = epd.get_frame_buffer(Image.open('demo/black.bmp'))
        frame_highlight[:] = epd.get_frame_buffer(Image.open('demo/highlight.bmp'))

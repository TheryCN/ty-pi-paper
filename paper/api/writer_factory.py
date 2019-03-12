from httplib2 import Http

import json
import os
from PIL import ImageFont

from countdown.config import Config
from countdown.writer import CountdownWriter
from image_writer import ImageWriter

class WriterFactory:

    config = Config()
    countdownWriter = CountdownWriter(config)
    imageWriter = ImageWriter()

    def get_writer(self, active):
        if active == 'countdown':
            return self.countdownWriter
        else:
            return self.imageWriter

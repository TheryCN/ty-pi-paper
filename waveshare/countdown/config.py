from __future__ import print_function

import json
import os

class Config:
    """ Configuration information.
    """

    config = {}

    def __init__(self):
        with open(self.countdown_path) as file:
            self.config = json.load(file)

    def get_countdown_uri(self):
        return self.config["countdownUri"];

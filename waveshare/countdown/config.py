from __future__ import print_function

import json
import os

class Config:
    """ Configuration information.
    """

    config = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    countdown_path = dir_path + "/config.json"

    def __init__(self):
        with open(selfds.countdown_path) as file:
            self.config = json.load(file)

    def get_countdown_uri(self):
        return self.config["countdownUri"];

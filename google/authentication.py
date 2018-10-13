from __future__ import print_function
from httplib2 import Http
from urllib.parse import urlencode

import json
import time
import sys
import os.path

class LimitedInputDeviceAuth:
    """ OAuth 2.0 for TV and Limited-Input Device Applications.
    """

    credentials = {}
    access_token = ""
    refresh_token = ""
    device_code = ""
    config = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    credentials_path = dir_path + "/resources/credentials.json"
    token_path = dir_path + "/resources/token.json"

    def __init__(self , config):
        self.credentials = {}
        self.config = config
        with open(self.credentials_path) as file:
            self.credentials = json.load(file)
        self.init_auth()

    def init_auth(self):
        if os.path.isfile(self.token_path):
            with open(self.token_path) as json_data:
                token_dict = json.load(json_data)
                self.access_token = token_dict["access_token"];

    def save_auth(self):
        token_dict = {}
        token_dict["access_token"] = self.access_token
        token_dict["refresh_token"] = self.refresh_token
        with open(self.token_path, 'w') as outfile:
            json.dump(token_dict, outfile)

    def auth_verification_url(self):
        # Step 1: Request device and user codes
        print("Step 1: Request device and user codes")
        content = self.request_device_and_user_codes()

        # Step 2: Handle the authorization server response
        self.device_code = content["device_code"];
        user_code = content["user_code"];
        verification_url = content["verification_url"]

        print("Step 2 : Device code {} / User code {} / Verification URL {}".format(self.device_code, user_code, verification_url))

        # Step 3: Display the user code
        print("Step 3: Display the user code")

        return "{0} - {1}".format(verification_url ,user_code)

    def auth(self):
        # Step 4: Poll Google's authorization server
        print("Step 4: Poll Google's authorization server")
        sys.stdout.flush()
        self.poll_auth_server(self.device_code)
        self.save_auth()

    def request_device_and_user_codes(self):
        data = {}
        data["client_id"] = self.credentials["client_id"]
        data["scope"] = self.config["calendarScope"]

        http_obj = Http()
        resp, content = http_obj.request(uri=self.config["requestDevice"] + "?" + urlencode(data), method='POST')

        return json.loads(content)

    def poll_auth_server(self, device_code):
        status = 0
        data = {}
        data["client_id"] = self.credentials["client_id"]
        data["client_secret"] = self.credentials["client_secret"]
        data["code"] = device_code
        data["grant_type"] = self.config["grantType"]

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        http_obj = Http()

        while status == 0:
            resp, content = http_obj.request(uri=self.config["requestToken"] + "?" + urlencode(data), method='POST', headers=headers)
            content = json.loads(content);
            if "error" in content:
                status = 0
            else:
                status = 1
                print(content)
                self.access_token = content["access_token"]
                self.refresh_token = content["refresh_token"]
            time.sleep(30)

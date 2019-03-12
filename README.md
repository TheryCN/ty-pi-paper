# Waveshare E-Ink Raspberry Project

1. Environment

Python version : Python 3.7
Raspberry pi 3 B+

Requirements :
* BCM2835 LIBRARY
* WIRINGPI LIBRARY

Python 3 libs :
* sudo apt-get install python3-pip
* sudo apt-get install python-imaging
* sudo pip3 install spidev
* sudo pip3 install RPi.GPIO
* sudo pip3 install Pillow

2. Hardware connection

Wiki : https://www.waveshare.com/wiki/2.9inch_e-Paper_Module_(C)

Documentation : https://www.waveshare.com/w/upload/5/55/2.9inch-e-paper-module-b-user-manual-en.pdf

3. Execution

Demo : python waveshare/main.py

Countdown : python waveshare/main_countdown.py (required ty-countdown)

4. API (flask)

pip install Flask

cd api

windows:
- py -m venv venv

raspberry:
- sudo pip3 install virtualenv
- virtualenv flaskenv

export FLASK_ENV=development
export FLASK_APP=app.py

flask run

#!/bin/sh
#chmod 755 startup.sh (executable)
sleep 10
cd /home/pi/Documents/GitHub/ty-raspberry-e-ink
git pull origin master
python3.5 main.py &

"""
Title        : RetroPie-Coin.py
Author       : zzeromin, member of Raspberrypi Village and Tentacle Team
Creation Date: Oct 15, 2017
Cafe         : http://cafe.naver.com/raspigamer
Blog         : http://rasplay.org, http://forums.rasplay.org/, https://zzeromin.tumblr.com/
Github       : https://github.com/rasplay, https://github.com/zzeromin
Thanks to    : Team Tentacle
Free and open for all to use. But put credit where credit is due.
"""

import RPi.GPIO as GPIO
import time

# check your SELECT gpio(BCM) pin number at https://pinout.xyz/
SELECT = 10 # GPIO BCM Number
SENSOR = 21 # GPIO BCM Number

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)
GPIO.setup(SELECT, GPIO.OUT)

try:
	while True:
		if GPIO.input(SENSOR) == GPIO.LOW:
			GPIO.output(SELECT, GPIO.HIGH)
		else:
			GPIO.output(SELECT, GPIO.LOW)
			print "Coin detected"
			time.sleep(0.05)

except KeyboardInterrupt:
	GPIO.cleanup()

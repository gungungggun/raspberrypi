#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

try:
    while True:
        if GPIO.input(12) == 1:
            GPIO.output(16, 1)
        else:
            GPIO.output(16, 0)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

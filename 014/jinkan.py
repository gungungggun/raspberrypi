#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        if GPIO.input(23) == GPIO.LOW:
            GPIO.output(24, GPIO.LOW)
        else:
            GPIO.output(24, GPIO.HIGH)
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

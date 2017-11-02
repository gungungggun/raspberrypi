#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

try:
    while True:
        if GPIO.input(12) == GPIO.LOW:
            print(GPIO.LOW)
        else:
            print(GPIO.HIGH)
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

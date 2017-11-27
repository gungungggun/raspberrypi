#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)

try:
    while True:
        GPIO.output(5, GPIO.HIGH)
        sleep(0.0005)
        GPIO.output(5, GPIO.LOW)
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)

GPIO.cleanup()

#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

count = 0
before = GPIO.HIGH

try:
    while True:
        if GPIO.input(12) == GPIO.LOW:
            if before == GPIO.HIGH:
                count = count + 1
                print(count)
            before = GPIO.LOW
        else:
            before = GPIO.HIGH
        if count % 2 == 0:
            GPIO.output(4, GPIO.LOW)
        else:
            GPIO.output(4, GPIO.HIGH)
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

sm = GPIO.PWM(18, 50)

sm.start(0.0)

sm.ChangeDutyCycle(12.0)
time.sleep(1)

sm.ChangeDutyCycle(2.5)
time.sleep(1)

sm.ChangeDutyCycle(7.25)
time.sleep(0.5)

sm.ChangeDutyCycle(2.5)
time.sleep(1)

GPIO.cleanup()

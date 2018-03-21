#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PWM = 18
IN1 = 24
IN2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

p = GPIO.PWM(PWM, 50)

GPIO.output(IN1, 1)
GPIO.output(IN2, 0)
p.start(100)
time.sleep(2)

GPIO.output(IN1, 0)
GPIO.output(IN2, 1)
p.start(100)
time.sleep(1)

GPIO.output(IN1, 1)
GPIO.output(IN2, 0)
p.start(100)
time.sleep(2)

GPIO.cleanup()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PWM1 = 18
IN1_1 = 23
IN1_2 = 24

PWM2 = 12
IN2_1 = 20
IN2_2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(IN1_1, GPIO.OUT)
GPIO.setup(IN1_2, GPIO.OUT)

GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(IN2_1, GPIO.OUT)
GPIO.setup(IN2_2, GPIO.OUT)

p1 = GPIO.PWM(PWM1, 50)
p2 = GPIO.PWM(PWM2, 50)

GPIO.output(IN1_1, 1)
GPIO.output(IN1_2, 0)
GPIO.output(IN2_1, 1)
GPIO.output(IN2_2, 0)
p1.start(100)
p2.start(100)
time.sleep(2)

GPIO.output(IN1_1, 1)
GPIO.output(IN1_2, 0)
GPIO.output(IN2_1, 0)
GPIO.output(IN2_2, 1)
p1.start(100)
p2.start(100)
time.sleep(2)

GPIO.output(IN1_1, 0)
GPIO.output(IN1_2, 1)
GPIO.output(IN2_1, 1)
GPIO.output(IN2_2, 0)
p1.start(100)
p2.start(100)
time.sleep(2)

GPIO.cleanup()

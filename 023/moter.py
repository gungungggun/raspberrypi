#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PWM1 = 18
IN1_1 = 24
IN1_2 = 25

PWM2 = 16
IN2_1 = 20
IN2_2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(IN1_1, GPIO.OUT)
GPIO.setup(IN1_2, GPIO.OUT)

GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(IN2_1, GPIO.OUT)
GPIO.setup(IN2_2, GPIO.OUT)

p1 = GPIO.PWM(PWM1, 10)
p2 = GPIO.PWM(PWM2, 10)
p1.start(0)
p2.start(0)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
GPIO.output(IN1_1, 1)
GPIO.output(IN1_2, 0)
GPIO.output(IN2_1, 1)
GPIO.output(IN2_2, 0)
p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100)
time.sleep(2)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
GPIO.output(IN1_1, 0)
GPIO.output(IN1_2, 0)
GPIO.output(IN2_1, 1)
GPIO.output(IN2_2, 0)
p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100)
time.sleep(2)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
GPIO.output(IN1_1, 1)
GPIO.output(IN1_2, 0)
GPIO.output(IN2_1, 0)
GPIO.output(IN2_2, 0)
p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100)
time.sleep(2)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
GPIO.output(IN1_1, 0)
GPIO.output(IN1_2, 1)
GPIO.output(IN2_1, 0)
GPIO.output(IN2_2, 1)
p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100)
time.sleep(2)

GPIO.cleanup()

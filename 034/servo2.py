#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

sm1 = GPIO.PWM(18, 50)
sm2 = GPIO.PWM(23, 50)

sm1.start(0.0)
sm2.start(0.0)

def move(sm, deg):
    a = 0.5
    b = 2.4
    hz = 50
    duty = a + (b - a) * ((deg + 90) / 180)
    par = duty / (1.0 / hz * 1000) * 100
    sm.ChangeDutyCycle(par)

move(sm1, 90.0)
time.sleep(0.5)
move(sm1, -60.0)
time.sleep(0.5)
move(sm2, 90.0)
time.sleep(0.5)
move(sm2, -60.0)
time.sleep(0.5)

move(sm1, 90.0)
move(sm2, 90.0)
time.sleep(0.5)
move(sm1, -60.0)
move(sm2, -60.0)
time.sleep(0.5)

GPIO.cleanup()

#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

sm = GPIO.PWM(18, 50)

sm.start(0.0)

def move(sm, deg):
    a = 0.5
    b = 2.4
    hz = 50
    duty = a + (b - a) * ((deg + 90) / 180)
    par = duty / (1.0 / hz * 1000) * 100
    sm.ChangeDutyCycle(par)
    time.sleep(1)

move(sm, 90.0)
move(sm, 0.0)
move(sm, -90.0)
move(sm, 0.0)
move(sm, 45.0)
move(sm, 0.0)
move(sm, 10.0)
move(sm, 0.0)
move(sm, -20.0)
move(sm, -20.0)
move(sm, 0.0)

GPIO.cleanup()

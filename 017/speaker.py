#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time

SPEAKER = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER, GPIO.OUT)

sp = GPIO.PWM(SPEAKER, 1)
sp.start(50)

sp.ChangeFrequency(100)
time.sleep(1)

sp.ChangeFrequency(200)
time.sleep(1)

sp.ChangeFrequency(300)
time.sleep(1)

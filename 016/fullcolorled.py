#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time

RED = 4
GREEN = 27
BLUE = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.HIGH)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)
time.sleep(1)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.HIGH)
GPIO.output(BLUE, GPIO.LOW)
time.sleep(1)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED, GPIO.HIGH)
GPIO.output(GREEN, GPIO.HIGH)
GPIO.output(BLUE, GPIO.LOW)
time.sleep(1)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.HIGH)
GPIO.output(BLUE, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED, GPIO.HIGH)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED, GPIO.HIGH)
GPIO.output(GREEN, GPIO.HIGH)
GPIO.output(BLUE, GPIO.HIGH)
time.sleep(1)

GPIO.cleanup()

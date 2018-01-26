#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class ShiftRegister:
    def __init__(self, sck, rck, si):
        self.sck = sck
        self.rck = rck
        self.si = si
        self.setup()

    def setup(self):
        print('setup')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sck, GPIO.OUT)
        GPIO.setup(self.rck, GPIO.OUT)
        GPIO.setup(self.si, GPIO.OUT)

    def cleanup(self):
        print('cleanup')
        GPIO.cleanup()

    def high(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def low(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def shift(self, pin):
        self.high(pin)
        self.low(pin)

    def reset(self):
        self.low(self.sck)
        self.low(self.rck)

    def send(self, nums):
        for num in nums:
            if num == 1:
                self.high(self.si)
            else:
                self.low(self.si)
            self.shift(self.sck)
        self.shift(self.rck)

class Light:
    def __init__(self):
        self.sr = ShiftRegister(12, 20, 21)

    def on(self, data, sleep = 1):
        for d in data:
	    self.sr.send(d)
            print(d)
            time.sleep(sleep)

    def cleanup(self):
        self.sr.cleanup()

light = Light()
data = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]
light.on(data, 0.2)
light.cleanup()

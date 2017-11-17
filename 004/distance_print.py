#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

TRIG_PIN = 21
ECHO_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)

try:
    while True:
        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.3)

        # 10us HIGH
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)

        # ECHO_PINがHIGHの時間計測
        while GPIO.input(ECHO_PIN) == 0:
            pass

        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass

        t = time.time() - start

        # 距離[cm] = (時間[s] / 2) * 音速[cm/s]
        v = 34000
        distance = (t / 2) * v
        print(distance, "cm")

except KeyboardInterrupt:
    pass

GPIO.cleanup()

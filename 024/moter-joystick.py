#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import spidev
import RPi.GPIO as GPIO

def getVolt(spi, ch):
    raw = spi.xfer2([1,(8+ch)<<4,0])
    raw2 = ((raw[1]&3) << 8) + raw[2]

    ref_volts = 5
    volts = (raw2 * ref_volts) / float(1023)
    volts = round(volts, 4)
    return volts

spi = spidev.SpiDev()
spi.open(0,0)

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

p1 = GPIO.PWM(PWM1, 100)
p2 = GPIO.PWM(PWM2, 100)
p1.start(0)
p2.start(0)
p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)

def run(x, y, p1, p2):
    yy = 2.5 - y
    if yy < 0:
        GPIO.output(IN1_1, 0)
        GPIO.output(IN1_2, 1)
        GPIO.output(IN2_1, 0)
        GPIO.output(IN2_2, 1)
    else:
        GPIO.output(IN1_1, 1)
        GPIO.output(IN1_2, 0)
        GPIO.output(IN2_1, 1)
        GPIO.output(IN2_2, 0)
    dc = abs(yy) * 40
    print(dc)
    p1.ChangeDutyCycle(dc)
    p2.ChangeDutyCycle(dc)
    time.sleep(0.01)

try:
    while True:
        x = getVolt(spi, 0)
        y = getVolt(spi, 1)
        print('x = ' + str(x))
        print('y = ' + str(y))
        run(x, y, p1, p2)
        print('-------------')
except KeyboardInterrupt:
    print('end')
finally:
    spi.close()
    GPIO.cleanup()

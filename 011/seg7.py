#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

CC1 = 21
CC2 = 20

A = 10
B = 9
C = 11
D = 5
E = 6
F = 13
G = 19
DP = 26

segs = [A, B, C, D, E, F, G]

numbers = [
    [A, B, C, D, E, F],
    [B, C],
    [A, B, D, E, G],
    [A, B, C, D, G],
    [B, C, F, G],
    [A, C, D, F, G],
    [A, C, D, E, F, G],
    [A, B, C, F],
    [A, B, C, D, E, F, G],
    [A, B, C, D, F, G],
]

def numberLight(num = 0, cc = 1):
    if num == None:
        return
    if cc == 1:
        GPIO.output(CC1, 1)
        GPIO.output(CC2, 0)
    else:
        GPIO.output(CC1, 0)
        GPIO.output(CC2, 1)

    for seg in segs:
        if seg in numbers[num]:
            GPIO.output(seg, 1)
        else:
            GPIO.output(seg, 0)

def number(num, t):
    strNum = str(num)
    if len(strNum) > 1:
        num1 = int(strNum[1])
        num2 = int(strNum[0])
    else:
        num1 = int(strNum[0])
        num2 = None

    count = 0
    start = time.time()
    while (time.time() - start < t):
        if count % 2 == 0:
            numberLight(num1, 1)
        else:
            numberLight(num2, 2)
        time.sleep(0.001)
        count = count + 1

GPIO.setup(CC1, GPIO.OUT)
GPIO.setup(CC2, GPIO.OUT)

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)

for i in range(100):
    number(i, 0.5)

GPIO.cleanup()

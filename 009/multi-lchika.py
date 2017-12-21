#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

A = 16
B = 20
C = 21

D = 13
E = 19
F = 26

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)

GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)

# 1つ目 点灯
GPIO.output(A, 1)
GPIO.output(B, 0)
GPIO.output(C, 0)
GPIO.output(D, 0)
GPIO.output(E, 1)
GPIO.output(F, 1)
time.sleep(0.5)

# 2つ目 点灯
GPIO.output(A, 1)
GPIO.output(B, 0)
GPIO.output(C, 0)
GPIO.output(D, 1)
GPIO.output(E, 0)
GPIO.output(F, 1)
time.sleep(0.5)

# 3つ目 点灯
GPIO.output(A, 1)
GPIO.output(B, 0)
GPIO.output(C, 0)
GPIO.output(D, 1)
GPIO.output(E, 1)
GPIO.output(F, 0)
time.sleep(0.5)

# 4つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 1)
GPIO.output(C, 0)
GPIO.output(D, 0)
GPIO.output(E, 1)
GPIO.output(F, 1)
time.sleep(0.5)

# 5つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 1)
GPIO.output(C, 0)
GPIO.output(D, 1)
GPIO.output(E, 0)
GPIO.output(F, 1)
time.sleep(0.5)

# 6つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 1)
GPIO.output(C, 0)
GPIO.output(D, 1)
GPIO.output(E, 1)
GPIO.output(F, 0)
time.sleep(0.5)

# 7つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 0)
GPIO.output(C, 1)
GPIO.output(D, 0)
GPIO.output(E, 1)
GPIO.output(F, 1)
time.sleep(0.5)

# 8つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 0)
GPIO.output(C, 1)
GPIO.output(D, 1)
GPIO.output(E, 0)
GPIO.output(F, 1)
time.sleep(0.5)

# 9つ目 点灯
GPIO.output(A, 0)
GPIO.output(B, 0)
GPIO.output(C, 1)
GPIO.output(D, 1)
GPIO.output(E, 1)
GPIO.output(F, 0)
time.sleep(0.5)

GPIO.cleanup()

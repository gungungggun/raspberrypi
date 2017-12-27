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

def light1(s = 0.1):
    GPIO.output(A, 1)
    GPIO.output(B, 0)
    GPIO.output(C, 0)
    GPIO.output(D, 0)
    GPIO.output(E, 1)
    GPIO.output(F, 1)
    sleep(s)

def light2(s = 0.1):
    GPIO.output(A, 1)
    GPIO.output(B, 0)
    GPIO.output(C, 0)
    GPIO.output(D, 1)
    GPIO.output(E, 0)
    GPIO.output(F, 1)
    sleep(s)

def light3(s = 0.1):
    GPIO.output(A, 1)
    GPIO.output(B, 0)
    GPIO.output(C, 0)
    GPIO.output(D, 1)
    GPIO.output(E, 1)
    GPIO.output(F, 0)
    sleep(s)

def light4(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 1)
    GPIO.output(C, 0)
    GPIO.output(D, 0)
    GPIO.output(E, 1)
    GPIO.output(F, 1)
    sleep(s)

def light5(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 1)
    GPIO.output(C, 0)
    GPIO.output(D, 1)
    GPIO.output(E, 0)
    GPIO.output(F, 1)
    sleep(s)

def light6(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 1)
    GPIO.output(C, 0)
    GPIO.output(D, 1)
    GPIO.output(E, 1)
    GPIO.output(F, 0)
    sleep(s)

def light7(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 0)
    GPIO.output(C, 1)
    GPIO.output(D, 0)
    GPIO.output(E, 1)
    GPIO.output(F, 1)
    sleep(s)

def light8(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 0)
    GPIO.output(C, 1)
    GPIO.output(D, 1)
    GPIO.output(E, 0)
    GPIO.output(F, 1)
    sleep(s)

def light9(s = 0.1):
    GPIO.output(A, 0)
    GPIO.output(B, 0)
    GPIO.output(C, 1)
    GPIO.output(D, 1)
    GPIO.output(E, 1)
    GPIO.output(F, 0)
    sleep(s)

try:
    while True:
        light1()
        light2()
        light3()
        light4()
        light5()
        light6()
        light7()
        light8()
        light9()

except KeyboardInterrupt:
    pass
GPIO.cleanup()

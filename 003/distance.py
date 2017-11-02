#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# HIGH or LOWの時計測
def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0
    # ECHO_PINがHIGHである時間を計測
    while GPIO.input(PIN) == end:
        t_start = time.time()

    while GPIO.input(PIN) == start:
        t_end = time.time()
    return t_end - t_start

# 距離計測
def calc_distance(TRIG_PIN, ECHO_PIN, LED_PIN, v=34000):
    try:
        while True:
            # TRIGピンを0.3[s]だけLOW
            GPIO.output(TRIG_PIN, GPIO.LOW)
            time.sleep(0.3)
            # TRIGピンを0.00001[s]だけ出力(超音波発射)
            GPIO.output(TRIG_PIN, True)
            time.sleep(0.00001)
            GPIO.output(TRIG_PIN, False)
            # HIGHの時間計測
            t = pulseIn(ECHO_PIN)
            # 距離[cm] = 音速[cm/s] * 時間[s]/2
            distance = v * t/2
            print(distance, "cm")
            if distance < 20:
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
    except KeyboardInterrupt:
        pass
    # ピン設定解除
    GPIO.cleanup()


# TRIGとECHOのGPIO番号
TRIG_PIN = 27
ECHO_PIN = 17
LED_PIN = 16

# 気温24[℃]の場合の音速[cm/s]
v = 33150 + 60*24

# ピン番号をGPIOで指定
GPIO.setmode(GPIO.BCM)
# TRIG_PINを出力, ECHO_PINを入力
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setwarnings(False)

# 距離計測(TRIGピン番号, ECHO_PIN番号, LEDピン, 音速[cm/s])
calc_distance(TRIG_PIN, ECHO_PIN, LED_PIN, v)

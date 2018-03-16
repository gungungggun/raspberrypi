#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import spidev

def getVolt(spi, ch):
    raw = spi.xfer2([1,(8+ch)<<4,0])
    raw2 = ((raw[1]&3) << 8) + raw[2]

    ref_volts = 5
    volts = (raw2 * ref_volts) / float(1023)
    volts = round(volts, 4)
    return volts

spi = spidev.SpiDev()
spi.open(0,0)

try:
    while True:
        getVolt(spi, 0)
        time.sleep(1)
except KeyboardInterrupt:
    print('end')
finally:
    spi.close()

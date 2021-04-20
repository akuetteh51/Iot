# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:17:35 2021

@author: root
"""

from machine import Pin,PWM
from time import sleep_ms

p32=Pin(value,Pin.IN)
slider=ADC(p32)
slider.atten(ADC.ATTN_11DB)

while True:
    print(slider.read())
    sleep_ms(300)
    
red=PWM(Pin(value,Pin.OUT))
grn=PWM(Pin(value,Pin.OUT))
blu=PWM(Pin(value,Pin.OUT))
red.freq(60)
grn.freq(60)
blu.freq(60)

r=0
g=0
b=0
steps =0

r=map(slider.read(),0,4095,0,255)
red.duty(r )
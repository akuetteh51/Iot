from machine import Pin as p
from time import sleep_ms as m
led = p(22,p.OUT)
while True:
    led.on()
    m(100)
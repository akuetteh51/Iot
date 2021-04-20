import neopixel
from machine import Pin as p
from time import sleep_ms
freq=877
n=26
np = neopixel.NeoPixel(p(n), freq)

np[0]=(23,45,100)
np.write()
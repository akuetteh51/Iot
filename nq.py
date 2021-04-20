import machine, neopixel
import time
n=21
freq=7
np = neopixel.NeoPixel(machine.Pin(n), freq)
np[0] = (0, 0, 0)
np.write()

while True:
    for i in range(0,255):
        np[0]=(i,0,0)
        np.write()
        print(i)

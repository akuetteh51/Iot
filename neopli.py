"""
Created on Thu Feb 16 16:47:35 2021
@author: MICHAEL NANA KWAME AKUETTEH
INDEX: PS/CSC/18/0002
"""
import machine, neopixel
import time
n=26
freq=7
a=[0,255]
b=[0,128]
np = neopixel.NeoPixel(machine.Pin(n), freq)
#pwm2 = PWM(Pin(19), freq=100, duty=i)
for n in range(-1,6):
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                np[0] = (a[i],a[j], a[k])
                print("("+str(a[i])+","+str(a[j])+","+str(a[k])+")")
    np.write()
    time.sleep(1)


for n in range(-1,6):
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                print("Decreasing the intensity:")
                np[n] = (b[i],b[j], b[k])
                print("("+str(b[i])+","+str(b[j])+","+str(b[k])+")")
    np.write()
    time.sleep(1)

np[0] = (0, 0, 0)
np.write()

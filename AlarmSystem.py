"""
Created on Thu Feb 16 16:47:35 2021

@author: MICHAEL NANA KWAME AKUETTEH
INDEX: PS/CSC/18/0002
"""


from machine import Pin as p
from machine import PWM as w
import neopixel
from time import sleep_ms
freq=7
n=26
np = neopixel.NeoPixel(p(n), freq)


pir = p(21, p.IN)
buza=p(18,p.OUT)
buz=w(buza)
buz.deinit()


def buzzer():
    buz.init()
    buz.freq(480)
    buz.duty(120)
    sleep_ms(100)
    buz.duty(0)
    #buz.deinit()
    
def off():
    for i in range(-1,6):
          np[i] = (0, 0, 0)
          np.write()
    
def on():
    for i in range(-1,6):
        
          np[i] = (255, 0, 0)
          np.write()
          


while True:
  
  if pir.value()==1:
      for i in range(0,5):
          on()
          sleep_ms(20)
          off()
          sleep_ms(20)
      
      buzzer()
      print("Motion Detected")
      sleep_ms(100)
  else:
      off()
      print("Motion Not Dectected")
      sleep_ms(500)

from machine import Pin as p
from time import sleep_ms

en=p(23,p.OUT)
l1=p(21,p.OUT)
l2=p(22,p.OUT)


while True:
#     en.value(1)
#     l1.value(1)
#     l2.value(0)
#     sleep_ms(900)
    print("clockwise")
    #en.value(1)
    #sleep_ms(50)
    en.value(1)
    l1.value(0)
    l2.value(1)
    sleep_ms(800)
    


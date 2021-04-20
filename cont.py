from machine import Pin as p
import time as t
#motorcl=p(21,p.OUT)#21
motorcl=p(21,p.OUT)#17
motorantcl=p(22,p.OUT)
#motorspd=p(16,p.OUT)

while True:
    motorcl.value(1)
    motorantcl.value(0)
    t.sleep_ms(100)
from machine import Pin as p
from time import sleep  
controlPin=[22,21,26,18]
for pin in controlPin:
    l=p(pin,p.OUT)
    l.value(0)
    
seq=[[1,0,0,0],
     [1,1,0,0],
     [0,1,0,0],
     [0,1,1,0],
     [0,0,1,0],
     [0,0,1,1],
     [0,0,0,1],
     [0,0,0,1]]
     
for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            l.value(seq[halfstep])
            sleep(0.001)
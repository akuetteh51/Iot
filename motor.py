
"""
Created on 22 Mar 21 16:47:35 2021

@author: MICHAEL NANA KWAME AKUETTEH
INDEX: PS/CSC/18/0002
"""
from machine import I2C
from machine import Pin as p
import time
import d1motor
i2c=I2C(1,scl=p(22),sda=p(21))
devices=i2c.scan()
print(devices)


A12=d1motor.Motor(0,i2c)
def Fowrard():
    for i in range(1,10,1):
        print("forward")
        A12.speed(1000*i)
        time.sleep(3)
        A12.brake()


def Backward():
    for i in range(1,10,1):
        print("Backward")
        A12.speed(-2000*i)
        time.sleep(3)
        A12.brake()

Forward()
Backward()

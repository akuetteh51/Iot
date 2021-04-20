from machine import Pin,I2C
from  time import sleep
import SHT

print("Scaning I2C address for ESP32")
scl=Pin(22)
sda=Pin(21)
i2c=I2C(1,scl=scl,sda=sda)
i2c_address=i2c.scan()

#Decimal Value
print(i2c_address)

#Hex Value
#print(hex(i2c_address[0]))
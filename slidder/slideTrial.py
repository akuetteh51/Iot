import network
import machine
from machine import PWM
import time
import random
import json
from umqtt.simple import MQTTClient

frequency=5000
led=machine.PWM(machine.Pin(19),frequency)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WorkShop', 'm,./@1234')
        
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
    
do_connect()



# Test reception e.g. with:
# mosquitto_sub -t foo_topic
CAYENNE_UNAME="d13e9410-9ec4-11eb-a2e4-b32ea624e442"
CAYENNE_PASSWORD="c848b0b8b2697a1a9d28e798d13d0288a6919c16"
CAYENNE_CLIENT= "0c995260-9ec6-11eb-a2e4-b32ea624e442"
server="mqtt.mydevices.com"

c = MQTTClient(CAYENNE_CLIENT, server,user=CAYENNE_UNAME, password=CAYENNE_PASSWORD)
    
val=[]    
try:
    c.connect()
    print("connection Success...")
except:
    print("connection Error...")

def onLED(topic,message):
     #switch= not led.value()
     #led.value(switch)
     
     val=message.decode('utf-8')
     val=val.split(',')
     print(val[1])
     i=int(val[1])
     led.duty(i)
     
     
     
     
c.set_callback(onLED)

topic="v1/"+CAYENNE_UNAME+"/things/"+CAYENNE_CLIENT+"/cmd/4"
bytes_topic=bytes(topic,'utf-8')

while True:
     c.subscribe(bytes_topic)
     
     
#      
# val=message.split(',')
#      
#      if val[1]==500:
#          led.freq(500)
#      elif val[1]==1000:
#          led.duty(1000)     

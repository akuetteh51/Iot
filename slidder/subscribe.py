import network
import machine
import time
import random
import json
from umqtt.simple import MQTTClient


led=machine.Pin(19,machine.Pin.OUT)

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
    
    
try:
    c.connect()
    print("connection Success...")
except:
    print("connection Error...")


#subscribing to a topic on cayenne
# def onLED(topic,message):
#      print(topic,":", message)
    
    
#subscribing to a topic on cayenne    
# A topic which will control the onboard LED on the ESP32    
def onLED(topic,message):
     switch= not led.value()
     led.value(switch)
     
     
     
     
     
c.set_callback(onLED)

topic="v1/"+CAYENNE_UNAME+"/things/"+CAYENNE_CLIENT+"/cmd/0"
bytes_topic=bytes(topic,'utf-8')

while True:
     c.subscribe(bytes_topic)




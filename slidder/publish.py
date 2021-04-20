import network
import machine
import time
import random
import json
from umqtt.simple import MQTTClient
import dht
#initializing the 
led=machine.Pin(19,machine.Pin.OUT)
temo=dht.DHT11(machine.Pin(22))
temo.measure()


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


topic="v1/"+CAYENNE_UNAME+"/things/"+CAYENNE_CLIENT+"/data/json"
bytes_topic=bytes(topic,'utf-8')


while True:
    try:
        randTemp= random.randrange(20,50,3)
        randHum=temo.humidity()
        devTemp= temo.temperature()
        data=[
        {
           "channel": 1,
           "value": randTemp,
           "type": "temp",
           "unit": "c"
    },
       
        {
           "channel": 2,
           "value": randTemp,
           "type": "temp",
           "unit": "c"
    },
        
         {
           "channel": 3,
           "value": randTemp,
           "type": "rel_hum",
           "unit": "p"
    }
    ]
     
        data=json.dumps(data)
        c.publish(bytes_topic,data)
        
       
        time.sleep(2)
    
    except OSError:
        print("Failed...")

    time.sleep(4)




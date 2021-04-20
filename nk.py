import network
import json
import random
from umqtt.simple import  MQTTClient
    
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WorkShop','m,./@1234')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
k = MQTTClient(client_id="2852f290-9ec6-11eb-a2e4-b32ea624e442", server="mqtt.mydevices.com", user="12257510-9ec6-11eb-b767-3f1a8f1211ba", password="8bf5b67f9111305c965ca02675f5865f2a24ec94")

    
def onLED(topic, msg):
    print(topic,":", msg)
k.set_callback(onLED)
#topic="V1/12257510-9ec6-11eb-b767-3f1a8f1211ba/things/2852f290-9ec6-11eb-a2e4-b32ea624e442/cmd/0"
topic="v1/12257510-9ec6-11eb-b767-3f1a8f1211ba/things/2852f290-9ec6-11eb-a2e4-b32ea624e442/data/json"
bytes_topic=bytes(topic,'utf-8')



while True:
    try:
        rndNumTemp = random.randrange(20,50,3)
        data = [
            {
                "channel": "1",
                "value":rndNumTemp,
                "topic": "temp",
                "unit":"c",
                
        
                
                
                }
            ]
        data = json.dumps(data)
        k.publish(bytes_topic,data)
        time.sleep(2)
    except OSError:
        print("failed...")
    time.sleep(4)
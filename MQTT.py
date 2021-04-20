from umqtt.simple import  MQTTClient
    
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ARMSTRONG','lolololo')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
k = MQTTClient(client_id="06e2a060-9f8e-11eb-a2e4-b32ea624e442", server="mqtt.mydevices.com", user="d9be5440-9ec4-11eb-a2e4-b32ea624e442", password="941bbcbe4e2bb825905b2f7459d1f9afe4208b55")

    
def onLED(topic, msg):
    print(topic,":", msg)
k.set_callback(onLED)
#topic="V1/12257510-9ec6-11eb-b767-3f1a8f1211ba/things/2852f290-9ec6-11eb-a2e4-b32ea624e442/cmd/0"
#v1/username/things/clientID/data/channel
topic="d9be5440-9ec4-11eb-a2e4-b32ea624e442/things/06e2a060-9f8e-11eb-a2e4-b32ea624e442/cmd/0"
bytes_topic=bytes(topic,'utf-8')
try :
    k.connect()
    k.subscribe(bytes_topic)
    print("connected successfully")
        

    
#         else:
#             k.check_msg()
#         # Then need to sleep to avoid 100% CPU usage (in a real
#         # app other useful actions would be performed instead)
#             time.sleep(1)
except OSError:
    print(" not connected")
    
while True:
        if True:
            # Blocking wait for message
            k.wait_msg()
        else:
            # Non-blocking wait for message
            k.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)
   


# 
# 
#     
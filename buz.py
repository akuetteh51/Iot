from machine import Pin , PWM
import time
# O closed 1 open

# al = Pin(16,Pin.IN,Pin.PULL_UP)

while True :
    #if al.value() == 1 :
    beep = PWM(Pin(22, Pin.OUT))
    beep.freq(440)
    beep.duty(512)
    time.sleep(5)
    beep.duty(0)
    beep.deinit()
    

from SHT import SHT30
from ST7735 import Display,color565
import fonts.sysfont as sysfont
from machine import SPI,Pin
from time import sleep

#display
sck=Pin(18)
mosi=Pin(23)
miso=Pin(19)
SPI_CS=26
SPI_DC=5
spi=SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)
#sht30
sensor=SHT30()
sensor.init(22,21)
temperature, humidity = sensor.measure()
display.clear()

display.draw_rectangle(3,1,113,15,color565(255, 253, 255))
display.draw_text(7, 5, 'SHT30 measurement', sysfont, color565(255, 253, 255))

#Temperature
display.draw_rectangle(1,20,15,71,color565(25, 123, 23))
#for i in range(0,9):
# display.draw_text(6, 7, '-', sysfont, color565(255,0, 0))
# display.draw_text(18, 6, '50', sysfont, color565(25, 123, 23))
display.draw_text(6, 20, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 20, '50', sysfont, color565(25, 123, 23))
display.draw_text(6, 34, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 34, '40', sysfont, color565(25, 123, 23))
display.draw_text(6, 48, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 48, '30', sysfont, color565(25, 123, 23))
display.draw_text(6, 61, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 61, '20', sysfont, color565(25, 123, 23))

display.draw_text(6, 74, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 74, '10', sysfont, color565(25, 123, 23))

display.draw_text(6, 85, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 85, '0', sysfont, color565(25, 123, 23))
#display.draw_rectangle(23,2,15,20,color565(25, 123, 23))
#display.show()
for i in range(88,temperature+16,-1):
    display.draw_vline(7,i,3,color565(0,210,244))
    display.draw_vline(8,i,3,color565(0,210,244))
    display.draw_vline(9,i,3,color565(0,210,244))
#     sleep(0.01)
#


display.draw_rectangle(80,20,15,71,color565(25, 123, 23))
display.draw_text(86, 20, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 20, '100', sysfont, color565(25, 123, 23))
display.draw_text(86, 34, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 34, '80', sysfont, color565(25, 123, 23))
display.draw_text(86, 48, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 48, '60', sysfont, color565(25, 123, 23))
display.draw_text(86, 61, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 61, '40', sysfont, color565(25, 123, 23))

display.draw_text(86, 74, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 74, '20', sysfont, color565(25, 123, 23))

display.draw_text(86, 85, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 85, '0', sysfont, color565(25, 123, 23))

# display.draw_text(86, 85, '-', sysfont, color565(255,0, 0))
# display.draw_text(99, 85, '0', sysfont, color565(25, 123, 23))

#for i in range(86,8,-1):
for i in range(86,humidity,-1):
    display.draw_vline(88,i,3,color565(0,210,244))
    display.draw_vline(89,i,3,color565(0,210,244))
    display.draw_vline(87,i,3,color565(0,210,244))
display.draw_text(71, 100, 'hummidity', sysfont, color565(25, 123, 23))
display.draw_text(71, 110, '{}%'.format(round(humidity,1)), sysfont, color565(255,250,240))
display.draw_text(-1, 100, "temperature", sysfont, color565(25, 123, 23))
display.draw_text(-1, 110, '{} degC'.format(round(temperature,1)), sysfont, color565(255,250,240))
#print(i)
#sleep(0.01)
# u'\u2103 for degree celcius
print("temp:",round(humidity,1),u'\u2103','RH:',round(humidity,1),'%')
#print(int(((86-humidity)/66)*100))
print(u'\xb0')
print(u'\u2103')
print(temperature/1.0)
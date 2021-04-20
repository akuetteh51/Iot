#from machine import Pin
from ST7735 import Display,color565
#from ST7735 import TFT
import fonts.sysfont as sysfont
from machine import SPI,Pin
from time import sleep


sck=Pin(18)
mosi=Pin(23)
miso=Pin(19)
SPI_CS=26
SPI_DC=5
spi=SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)
#display.draw_text(0, 0, 'Hello World!', sysfont, color565(255, 0, 0))
display.clear()
display.draw_rectangle(1,7,15,85,color565(25, 123, 23))
#for i in range(0,9):
display.draw_text(6, 7, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 6, '50', sysfont, color565(25, 123, 23))
display.draw_text(6, 20, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 20, '40', sysfont, color565(25, 123, 23))
display.draw_text(6, 34, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 34, '30', sysfont, color565(25, 123, 23))
display.draw_text(6, 48, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 48, '20', sysfont, color565(25, 123, 23))
display.draw_text(6, 61, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 61, '10', sysfont, color565(25, 123, 23))

display.draw_text(6, 74, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 74, '5', sysfont, color565(25, 123, 23))

#display.draw_text(27, 84, '-', sysfont, color565(255,0, 0))
#display.draw_text(35, 10, '0', sysfont, color565(25, 123, 23))

display.draw_text(6, 85, '-', sysfont, color565(255,0, 0))
display.draw_text(18, 85, '0', sysfont, color565(25, 123, 23))

#display.draw_text(2, 95, 'temp', sysfont, color565(255, 0, 0))
#display.draw_rectangle(23,2,15,20,color565(25, 123, 23))
#display.show()
for i in range(82,8,-1):
    display.draw_vline(8,i,10,color565(0,210,244))
    sleep(0.01)
    
    
display.draw_rectangle(80,7,15,85,color565(25, 123, 23))
#for i in range(0,9):
display.draw_text(86, 7, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 6, '50', sysfont, color565(25, 123, 23))
display.draw_text(86, 20, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 20, '40', sysfont, color565(25, 123, 23))
display.draw_text(86, 34, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 34, '30', sysfont, color565(25, 123, 23))
display.draw_text(86, 48, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 48, '20', sysfont, color565(25, 123, 23))
display.draw_text(86, 61, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 61, '10', sysfont, color565(25, 123, 23))

display.draw_text(86, 74, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 74, '5', sysfont, color565(25, 123, 23))

#display.draw_text(27, 84, '-', sysfont, color565(255,0, 0))
#display.draw_text(35, 10, '0', sysfont, color565(25, 123, 23))

display.draw_text(86, 85, '-', sysfont, color565(255,0, 0))
display.draw_text(99, 85, '0', sysfont, color565(25, 123, 23))

#display.draw_text(60, 95, 'hummidity', sysfont, color565(255, 0, 0))
#display.draw_rectangle(23,2,15,20,color565(25, 123, 23))
#display.show()
for i in range(86,8,-1):
    display.draw_vline(88,i,3,color565(0,210,244))
    display.draw_text(120, 100, 'hummidity: {}'.format(((86-i)/77)*50), sysfont, color565(255, 0, 0))
    print(i)
    sleep(0.01)
    
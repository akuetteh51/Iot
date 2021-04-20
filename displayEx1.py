
from ST7735 import Display,color565
import ST7735 as l
import fonts.sysfont as sysfont
import fonts.courier20 as courier2
import fonts.EspressoDolce18x24 as EspressoDolce18x24
from machine import SPI,Pin
from time import sleep
from random import randint ,seed

#display
seed(10)
sck=Pin(18)
mosi=Pin(23)
miso=Pin(19)
SPI_CS=26
SPI_DC=5
spi=SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)

display.clear()
for i in range(0,51):
    display.line(randint(0,255),randint(0,255),randint(0,255),randint(0,255),color565(randint(0,255),randint(0,255), randint(0,255)))
sleep(5) 
display.show()
   
display.clear()
for i in range(0,51):
 display.draw_rectangle(randint(0,255),randint(0,255),randint(0,255),randint(0,255),color565(randint(0,255),randint(0,255), randint(0,255)))
sleep(5)
display.clear()
for i in range(0,51):
    display.draw_circle(randint(0,101),randint(0,101),randint(0,101),color565(randint(0,101),randint(0,101), randint(0,101)))
sleep(5)
display.clear()

display.draw_text(6, 20, 'DSCIT', sysfont, color565(255,0, 0))
#ST7735.rotation(45)
display.draw_text(12, 5, 'DSCIT', courier2, color565(0,255, 0))


display.draw_text(20, 50, 'DSCIT',EspressoDolce18x24, color565(0,0,255))

display.draw_text(30, 20, 'DSCIT', sysfont, color565(255,0, 0),landscape=True)
#ST7735.rotation(45)
display.draw_text(32, 5, 'DSCIT', courier2, color565(0,255, 0),landscape=True)


display.draw_text(34, 50, 'DSCIT',EspressoDolce18x24, color565(0,0,255),landscape=True)



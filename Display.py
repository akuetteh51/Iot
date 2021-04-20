from ST7735 import Display,color565
import fonts.sysfont as sysfont
from machine import SPI,Pin
from time import sleep


spi=SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)

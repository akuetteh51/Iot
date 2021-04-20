from SHT import SHT30

sensor=SHT30()
sensor.init(22,21)

temperature, humidity = sensor.measure()
print("temp:",temperature,'ºC','RH:',humidity,'%')
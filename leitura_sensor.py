# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Sensor:
  def __init__(self): #sem parametros
    print('Objeto Sensor inicializado!')
  
  def getQtde(self):
    return 3;

  def getData(self, i):
    if i==1:
      u, t = Adafruit_DHT.read(Adafruit_DHT.DHT11, 4)
    elif i==2:  
      u, t = Adafruit_DHT.read(Adafruit_DHT.DHT11, 17)
    elif i==3:  
      u, t = Adafruit_DHT.read(Adafruit_DHT.DHT22, 27) # funciona ok
      #umid3, temp3 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 27)
    return t, u

if __name__ == '__main__':
  umid1, temp1 = Adafruit_DHT.read(Adafruit_DHT.DHT11, 4)
  umid2, temp2 = Adafruit_DHT.read(Adafruit_DHT.DHT11, 17)
  umid3, temp3 = Adafruit_DHT.read(Adafruit_DHT.DHT22, 27) # funciona ok
  #umid3, temp3 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 27)

  if umid1 is not None and temp1 is not None:
    print("Sensor 1 > Temperatura:",temp1, 'umidade:',umid1);
  else:
    print("Sensor 1 > Falha ao ler dados!")  

  if umid2 is not None and temp2 is not None:
    print("Sensor 2 > Temperatura:",temp2, 'umidade:',umid2);
  else:
    print("Sensor 2 > Falha ao ler dados!")

  if umid3 is not None and temp3 is not None:
    print("Sensor 3 > Temperatura: {:.2f}".format(temp3), 'umidade: {:.2f}'.format(umid3))
  else:
    print("Sensor 3 > Falha ao ler dados!")



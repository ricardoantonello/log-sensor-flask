from app import app # from app=modulo import app=variavel em __init__ do modulo principal



# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)





@app.route('/')
def index():

    umid1, temp1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    if umid1 is not None and temp1 is not None:
      return "Sensor 1 > Temperatura: {:.2f}. Umidade: {:.2f}.".format(temp1,umid1)
    else:
      return "Sensor 1 > Falha ao ler dados!"

    

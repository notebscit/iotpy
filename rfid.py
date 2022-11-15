import RPi.GPIO as GPIO
import mfrc522 as simpleMFRC522
reader=SimpleMFRC522.simpleMFRC522()
#code for write
##try:
##    text=input("New Data")
##    print("Now place your tsg to write")
##    reader.write(text)
##    print("Written")
##finally:
##    GPIO.clenup()

#code to read
try:
    id,text=reader.read()
    print(id)
    print(text)
finally:
    GPIO.clenup()



##connection
##
##pin1-ceo of rpi
##sck-sclk
##mosi-mosi
##mios-mios
##rq-nocon
##gnd-gnd
##rst-25
##3.3v-3v3


#enable spi
#sudo apt-get update/upgrade
#sudo apt-get install python 2.7-dev
#git clone https://github.com/lthiery/SPI-Py
#cd SPI-PY
#sudo python install setup.py
#git clone https://github.com/pimylifeup/MFRC522-python
#cd MFRC522

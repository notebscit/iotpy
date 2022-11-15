import time
import matplotlib.pyplot as plt
from drawnow import*
import Adafruit_ADS1x15
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
VAL=[]
CNT=0
plt.ion()
ada.start_ada(0,gain=GAIN)
print("Reading ADS1x15 channel 0")

def makeFig():
    plt.ylim(-5000,5000)
    plt.title('Oscilloscope')
    plt.grid(True)
    plt.ylabel("ADC output")
    plt.plot(val,'ro-',label='channel 0')
    plt.legent(loc='lower right')


while True:
    value=adc.get_last_result()
    print('channel 0:{0}'.format(value))


    time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(0.000001)
    cnt=cnt+1
    if(cnt>50):
        val.pop(0)

    



#vDD-3.3V
#SCL-SCL
#SDA-SDA
#ADDR-GND
#AO-1LEG OF POTENTI




#enable I2C    
#sudo apt-get update/upgrade
#sude apt-get install build-essential pythod-dev python-smbus git
#sudo apt-get install I2C-tools
#create folder
#cd to folder
#git clone https://github.com/adafruit/Adafruit_python_ADS1x15
#cd to Adafruit_python_ADS1x15
#sudo install python Setup.py install
#cd examples
#pytthon simpletest.py

#graph & drawing

#sudo apt-get install python-matplotlib/python-pip
#sude pip install drawnow
#sudo nano scope.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

list=[5,6,13,19,26]


##running model
##while True:
##    for num in range(len(list)):
##        GPIO.output(list[num],GPIO.HIGH)
##        time.sleep(0.5)
##        GPIO.output(list[num],GPIO.LOW)
##        time.sleep(0.5)


#pingpong
##while True:
##    for num in range(len(list)):
##        GPIO.output(list[num],GPIO.HIGH)
##        time.sleep(0.5)
##        GPIO.output(list[num],GPIO.LOW)
##        time.sleep(0.5)
##    for num in range(len(list)):
##        GPIO.output(list[len(list)-num-1],GPIO.HIGH)
##        time.sleep(0.5)
##        GPIO.output(list[len(list)-num-1],GPIO.LOW)
##        time.sleep(0.5)

#center dash

while True:
    for num in range(int(len(list)/2)+1):
        GPIO.output(list[num],GPIO.HIGH)
        GPIO.output(list[len(list)-num-1],GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(list[num],GPIO.LOW)
        GPIO.output(list[len(list)-num-1],GPIO.LOW)






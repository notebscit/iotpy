











import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
segments =  (17,27,22,23,24,25,5,6)
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
digits = (16,20,12,21)
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
 
while True:
    n = time.ctime()[11:13]+time.ctime()[14:16]
    s = str(n).rjust(4)
    for digit in range(4):
        for loop in range(0,7):
            GPIO.output(segments[loop], num[s[digit]][loop])
            if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                GPIO.output(25, 1)
            else:
                GPIO.output(25, 0)
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)
GPIO.cleanup()
    
   






   
##connection
##1 24
##2 23
##3 6
##4 22
##5 5
##6 12
##7 27
##8 21
##9 20
##10 25
##11 17 
##12 16


    

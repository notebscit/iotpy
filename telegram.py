import RPi.GPIO as GPIO
import telepot
import time
from telepot.Loop import MessageLoop
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)
green=6
yellow=19
red=13
white=26
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(white,GPIO.OUT)

GPIO.output(green,0)
GPIO.output(yellow,0)
GPIO.output(red,0)
GPIO.output(white,0)

def action(msg):
    chat_id=msg['chat']['id']
    command=msg['text']
    list=[green,yellow,red,white]
    if 'on' in command:
        message="Turned on"
        if 'white' in command:
            message=message+"white"
            GPIO.output(white,1)
        if 'red' in command:
            message=message+"red"
            GPIO.output(red,1)
        if 'yellow' in command:
            message=message+"yellow"
            GPIO.output(yellow,1)
        if 'green' in command:
            message=message+"green"
            GPIO.output(green,1)
        if 'all' in command:
            message=message+"all"
            GPIO.output(list,1)
            
        telegram_bot.sendMessage(chat_id,message)

    if 'off' in command:
        message="Turned off"
        if 'white' in command:
            message=message+"white"
            GPIO.output(white,0)
        if 'red' in command:
            message=message+"red"
            GPIO.output(red,0)
        if 'yellow' in command:
            message=message+"yellow"
            GPIO.output(yellow,0)
        if 'green' in command:
            message=message+"green"
            GPIO.output(green,0)
        if 'all' in command:
            message=message+"all"
            GPIO.output(list,0)
        telegram_bot.sendMessage(chat_id,message)

    telegram_bot=telepot.Bot("botid")
    print(telegram_bot.getMe())
    MessageLoop(telegram_bot,action).run_as_thread()
    print("UP and running")
    while 1:
        time.sleep(10)



#26-w
#19-y
#13-r
#6-g

#
#
#sudo apt-get update/upgrade
#sudo apt-get install python-pip
#sudo pip install telepot

    

    

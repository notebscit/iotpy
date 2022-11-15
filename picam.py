from picamera import Picamera
from time import sleep
camera=Picamera()
camera.vflip=True
camera.start_preview()
sleep(5)
camera.Capture("fileloc .jpg")
camera.stop_preview()




##from picamera import Picamera
##from time import sleep
##camera=Picamera()
##camera.vflip=True
##camera.start_preview()
##sleep(5)
##camera.Capture("fileloc .h264")
##camera.stop_recording()
##camera.stop_preview()

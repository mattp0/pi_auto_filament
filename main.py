import RPi.GPIO as GPIO
import time

channel=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while 1:
    res = GPIO.input(channel)
    if res:
        print("filament detected: ", res)
    else:
        print("Filament not detected: ", res)
    time.sleep(2)

import RPi.GPIO as GPIO

channel=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while 1:
    res = GPIO.input(channel)
    print("gpio at channel: ", channel)
    if res:
        print("filament detected: ", res)
    else:
        print("Filament not detected. ", res)

print()

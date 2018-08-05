import time #So I can get the time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BOARD)
chan_list = [5] #This is the list of pins that I want to be GPIO pins
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(5, 1)
Epoch = bin(int(time.time())) #get the time in binary
print Epoch


GPIO.cleanup()

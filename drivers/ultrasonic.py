import RPi.GPIO as GPIO
import time

trigger = 14
echo = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trigger, True)
    time.sleep(0.00001) # Set trigger to high for 10 microseconds.
    GPIO.output(trigger, False)

    startTime = time.time()
    stopTime = time.time()

    while GPIO.input(echo) == 0: # The echo pulse back has not yet started
        startTime = time.time()

    while GPIO.input(echo) == 1: # The echo pulse is still going.
        stopTime = time.time()

    return ((stopTime - startTime)*34300)/2 # Distance is the time it took to receive a signal, multiplied by the speed of sound, divided by 2 since signal goes to and from ultrasonic sensor.

while True:
    print(distance())
    time.sleep(1)

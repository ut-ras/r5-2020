"""
This file contains the interface for driving the emergency stop button, placed on the top of the robot.
Filename: stop_button.py
Author: Matthew Yu
Last Modified: 2/20/20
Notes: 
    * pins need to be adjusted for the final robot configuration
    * the buttonEventHandler should connect to a global variable that our main should be able to see; the main should act upon the variable being True (i.e. emergency_stop=True), stopping all functionality but not actually shutting off.
    * Potentially, the emergency stop button should also act as a start button. TODO: Consider.
    * possible useful documents: 
        * http://raspberrywebserver.com/gpio/using-interrupt-driven-gpio.html
        * https://medium.com/@rxseger/interrupt-driven-i-o-on-raspberry-pi-3-with-leds-and-pushbuttons-rising-falling-edge-detection-36c14e640fef
        * https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
        * https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import pins as p
import config as c
import threading as t
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

# TODO: for testing purposes, set button and LED to GPIO 9, 10. 
# Make sure that the default pull according to the rpi datasheet is pull down low.
PIN_SW=9
PIN_LED=10

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

event = t.Event()
# sets up the GPIO pins used for the button.
def setup():
    GPIO.setup(PIN_SW, GPIO.IN) # Set pin 9 to be an input pin (switch)
    GPIO.setup(PIN_LED, GPIO.OUT) # Set pin 10 to be an output pin (LED)

    # declare a handler interrupt on input pin
    GPIO.add_event_detect(PIN_SW, GPIO.RISING, callback=buttonEventHandler, bouncetime=200) # looking for a rising edge

def shutdown():
    GPIO.cleanup(PIN_SW, GPIO.IN)
    GPIO.cleanup(PIN_LED, GPIO.OUT)

# TODO: handler sets a flag in your supposed main; upon receiving that the main program must halt its state.
def buttonEventHandler():
    # do something - right now let's just turn on an LED.
    GPIO.output(PIN_LED, GPIO.HIGH)
    event.wait(1)
    GPIO.output(PIN_LED, GPIO.LOW)
    if c.emergency_stop is True:
        c.emergency_stop = False
    else:
        c.emergency_stop = True 

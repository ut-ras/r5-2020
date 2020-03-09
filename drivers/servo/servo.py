"""
This file contains the interface for driving the HD-1501MG servo that controls the bin.
Filename: servo.py
Author: Matthew Yu
Last Modified: 2/21/20
Notes: 
    * pins need to be adjusted for the final robot configuration
    * the servo should be able to move to two positions:
        * at rest (0 deg)
        * full extension (150 deg)
    * the servo should be called by the main thread.
    * possible useful documents: 
        * http://bc-robotics.com/datasheets/HD-1501MG.pdf
        * https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
    * assumptions made: that the servo needs a continuous signal to maintain position.

"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import pins as p
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

"""
I want the servo to start at the minimum position (800us=.8ms) and go to the maximum position (2200us=2.2ms).

To do that, let's set the frequency such that 1 full cycle is roughly 2.2ms: 454 Hz according to https://www.unitjuggler.com/convert-frequency-from-Hz-to-ms(p).html?val=454 .

To get the maximum position, we know duty cycle should be 100% of 454 Hz.

To get the minimum position, we need a ratio of 2.2ms that is equal to .8ms: .8/2.2 = .3636..

Therefore, 36.4% is the approximate expected duty cycle.
"""

FREQ_SERVO = 454 #Hz

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

pwm = None # initialize software PWM object.

def setup():
    print("Setup of the HD-1501MG Servo.")
    GPIO.setup(p.SERVO,  GPIO.OUT) # Set pin 9 to be an input pin (switch)
    pwm = GPIO.PWM(p.SERVO, FREQ_SERVO)
    pwm.start(100.0) 

def shutdown():
    pwm.stop()
    GPIO.cleanup(p.SERV0)

def rest(): # start out in the max position.
    pwm.ChangeDutyCycle(100.0) 
    
def extend(): # go to the min position
    pwm.ChangeDutyCycle(36.4)
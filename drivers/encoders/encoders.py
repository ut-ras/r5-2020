"""
This file contains the interface for reading the encoders on the 37D Metal Gearmotors.
Filename: encoders.py
Author: Matthew Yu
Last Modified: 2/21/20
Notes:
    * Motor Datasheet: https://www.pololu.com/file/0J1736/pololu-37d-metal-gearmotors-rev-1-2.pdf
    * A possible solution to read ticks is to interrupt on high and increment a counter.
    * Proposed operation:
        setup()
        ...
        shutdown()
"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import time
import pins as p
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

# list of channels touched by encoders.
chan_list = [
    p.AOUT1,
    p.BOUT1,
    p.AOUT2,
    p.BOUT2,
    p.AOUT3,
    p.BOUT3,
    p.AOUT4,
    p.BOUT4
]

ENC1_count = 0
ENC2_count = 0
ENC3_count = 0
ENC4_count = 0

# sets up the GPIO pins used for the motor encoders.
def setup():
    print("Setup Encoders.")
    GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set all touched pins to input mode

    # declare a handler interrupt on input pin
    for channel in chan_list:
        GPIO.add_event_detect(channel, GPIO.RISING, callback=encoderEventHandler)

# cleans all channels touched by motor controller
def shutdown():
    GPIO.cleanup(chan_list)

# increments a tick on the rising edge of an encoder pin.
def encoderEventHandler(channel):
    if channel is p.AOUT1 or p.BOUT1:
        global ENC1_count
        ENC1_count += 1
    elif channel is p.AOUT2 or p.BOUT2:
        global ENC2_count
        ENC2_count += 1
    elif channel is p.AOUT3 or p.BOUT3:
        global ENC3_count
        ENC3_count += 1
    elif channel is p.AOUT4 or p.BOUT4:
        global ENC4_count
        ENC4_count += 1
    else:
        print("Invalid channel: " + str(channel))

# read returns the ticks given the encoder id.
# use: when you want to know ticks after moving (and therefore to calculate distance).
def read(enc_val):
    if enc_val is 1:
        return ENC1_count
    elif enc_val is 2:
        return ENC2_count
    elif enc_val is 3:
        return ENC3_count
    elif enc_val is 4:
        return ENC4_count
    else:
        print("Invalid read enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

# reset takes the given encoder id and resets its ticks.
# use: when changing direction and ENCx_count is no longer useful.
def reset(enc_val):
    if enc_val is 1:
        global ENC1_count
        ENC1_count = 0
    elif enc_val is 2:
        global ENC2_count
        ENC2_count = 0
    elif enc_val is 3:
        global ENC3_count
        ENC3_count = 0
    elif enc_val is 4:
        global ENC4_count
        ENC4_count = 0
    else:
        print("Invalid reset enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

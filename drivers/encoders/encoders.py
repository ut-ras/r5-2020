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
import config as c
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

"""
GENERAL_PURPOSE_COMMANDS - used for state changes
"""
# sets up the GPIO pins used for the motor encoders.
def setup():
    print("Setup Encoders.")
    GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set all touched pins to input mode

    # declare a handler interrupt on input pin
    for channel in chan_list:
        GPIO.add_event_detect(channel, GPIO.RISING, callback=encoderEventHandler)
        GPIO.add_event_detect(channel, GPIO.FALLING, callback=encoderEventHandler)
# cleans all channels touched by motor controller
def shutdown():
    print("Shutdown Encoders.")
    GPIO.cleanup(chan_list)

"""
Say we have a 3in. radius wheel - the circumference is 18.85in.
Consider if we only get 16 ticks per revolution (only rise/fall of one encoder).
That is:  16 ticks      1 tick      360 degs
            -----   =   ------   x   -----     = 0.85 ticks per in  = 1.176 in per tick
          360 degs    22.5 degs     18.85 in

Now consider 64 ticks per revolution (rise/fall of both encoders).
That is:  64 ticks      1 tick      360 degs
            -----   =   ------   x   -----     = 3.40 ticks per in  = 0.295 in per tick
          360 degs    5.625 degs    18.85 in

Massive change in resolution! If we are by a couple ticks, that means we may be off
by several inches if we decide to only look at one encoder.

To reduce this lack of resolution, we can use smaller mechanum wheels. Below
are the resolutions for a 50mm. radius wheel (the one we are using).
31.42 * 22.5 / 360 =  1.96 cm / tick
31.42 * 5.625 / 360 = 0.49 cm / tick

Obviously, real world results will vary, but I hope this is enough justification to:
    1 - take as much encoder resolution as you can
    2 - use small wheels! You may move slower, but you will move more accurately.
"""
# increments a tick on the rising edge of an encoder pin.
def encoderEventHandler(channel):
    if channel is p.AOUT1 or p.BOUT1:
        global c.ENC1_count
        c.ENC1_count += 1
    elif channel is p.AOUT2 or p.BOUT2:
        global c.ENC2_count
        c.ENC2_count += 1
    elif channel is p.AOUT3 or p.BOUT3:
        global c.ENC3_count
        c.ENC3_count += 1
    elif channel is p.AOUT4 or p.BOUT4:
        global c.ENC4_count
        c.ENC4_count += 1
    else:
        print("Invalid channel: " + str(channel))
        print("Choose a value between [1, 4].")

# read returns the ticks given the encoder id.
# use: when you want to know ticks after moving (and therefore to calculate distance).
def read(enc_val):
    if enc_val is 1:
        return c.ENC1_count
    elif enc_val is 2:
        return c.ENC2_count
    elif enc_val is 3:
        return c.ENC3_count
    elif enc_val is 4:
        return c.ENC4_count
    else:
        print("Invalid read enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

# reset takes the given encoder id and resets its ticks.
# use: when changing direction and ENCx_count is no longer useful.
def reset(enc_val):
    if enc_val is 1:
        global c.ENC1_count
        c.ENC1_count = 0
    elif enc_val is 2:
        global c.ENC2_count
        c.ENC2_count = 0
    elif enc_val is 3:
        global c.ENC3_count
        c.ENC3_count = 0
    elif enc_val is 4:
        global c.ENC4_count
        c.ENC4_count = 0
    else:
        print("Invalid reset enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

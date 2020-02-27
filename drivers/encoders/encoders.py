"""
This file contains the interface for reading the encoders on the 37D Metal Gearmotors.
Filename: encoders.py
Author: Matthew Yu
Last Modified: 2/26/20
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
import config
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

# list of channels touched by encoders.
chan_list = [
    p.ENC_FR,
    p.ENC_FL,
    p.ENC_BL,
    p.ENC_BR
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
# cleans all channels touched by motor controller
def shutdown():
    print("Shutdown Encoders.")
    GPIO.cleanup(chan_list)

"""
Say we have a 3in. radius wheel - the circumference is 18.85in.
Consider if we only get 16 ticks per revolution (only rise/fall of one encoder).
We want to multiply the tick/degs by the motor gearing ratio (output ticks/degs).
Now we want ticks/in - multiply the result by 360 degs/circumference.
Flip it to get in/tick.

That is:  16 ticks      1 tick     102.08     360 degs
            -----   =   ------   x ------- x  --------     = 86.646 ticks per in  = 0.0115 in per tick
          360 degs     22.5 degs      1       18.85 in

If we upped the resolution to 64 ticks/resolution, you will notice that the in/tick will drop dramatically (by a factor of 4)!

The wheel radius for our robot has been determined to be 50 mm. Using the procedure above, we obtain the resolutions below.

31.42 (circumference in cm) *  22.5  / 360 / 102.08 =  0.019 cm / tick  (.19 mm / tick)
31.42 (circumference in cm) *  5.625 / 360 / 102.08 = 0.0049 cm / tick  (.048 mm / tick)

It appears that with a 16 tick/resolution, we get a good accuracy. As a result, let's define our system to use the rising edge of one encoder for each motor (16 ticks/motor revolution).

The next step is to test for precision.

As an aside, real world results of the tick resolution accuracy can vary. As a general rule, you can get more resolution by:
    1 - take as much encoder resolution as you can
    2 - use small wheels! You may move slower, but you will move more accurately.
"""
# increments a tick on the rising edge of an encoder pin.
def encoderEventHandler(channel):
    if channel is p.ENC_FR:
        config.ENC1_count += 1
    elif channel is p.ENC_FL:
        config.ENC2_count += 1
    elif channel is p.ENC_BL:
        config.ENC3_count += 1
    elif channel is p.ENC_BR:
        config.ENC4_count += 1
    else:
        print("Invalid channel: " + str(channel))
        print("Choose a value between [1, 4].")

# read returns the ticks given the encoder id.
# use: when you want to know ticks after moving (and therefore to calculate distance).
def read(enc_val):
    if enc_val is config.FRONT_RIGHT:
        return config.ENC1_count
    elif enc_val is config.FRONT_LEFT:
        return config.ENC2_count
    elif enc_val is config.BACK_LEFT:
        return config.ENC3_count
    elif enc_val is config.BACK_RIGHT:
        return config.ENC4_count
    else:
        print("Invalid read enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

# reset takes the given encoder id and resets its ticks.
# use: when changing direction and ENCx_count is no longer useful.
def reset(enc_val):
    if enc_val is config.FRONT_RIGHT:
        config.ENC1_count = 0
    elif enc_val is config.FRONT_LEFT:
        config.ENC2_count = 0
    elif enc_val is config.BACK_LEFT:
        config.ENC3_count = 0
    elif enc_val is config.BACK_RIGHT:
        config.ENC4_count = 0
    else:
        print("Invalid reset enc_val: " + str(enc_val))
        print("Choose a value between [1, 4].")

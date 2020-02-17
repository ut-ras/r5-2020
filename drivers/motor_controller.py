"""
This file contains the interface for driving the VNH5019A-E motor driver.
Filename: motor_controller.py
Author: Matthew Yu
Last Modified: 2/16/20
Notes: 
    * How a Mecanum Drive Works: https://seamonsters-2605.github.io/archive/mecanum/
    * Motor Driver data sheet and logic table: https://www.pololu.com/file/0J504/vnh5019.pdf
    * RPI4 R5 Moving Base Pinout: https://docs.google.com/spreadsheets/d/1HRyUoHULSqokP9kBjE0gk1rphJi5dLCR_PKfli7fx-g/edit#gid=1188077649
    TODO: Update pins used after moving base checkpoint, if needed
    TODO: determine whether to have an input parameter countdown timer that calls stop after use.
"""
import pins as p
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

# list of channels touched by motor controller.
chan_list = [
    p.INA1,    # Motor Driver 1 (Front Right)
    p.INB1,
    p.INA2,    # Motor Driver 2 (Front Left)
    p.INB2,
    p.INA3,    # Motor Driver 3 (Back Left)
    p.INB3,
    p.INA4,    # Motor Driver 4 (Back Right)
    p.INB4
]

# sets up the GPIO pins used for the motor controllers.
def setup():
    GPIO.setup(chan_list, GPIO.OUT)
# cleans all channels touched by motor controller
def shutdown():
    GPIO.cleanup(chan_list, GPIO.OUT)

"""
See the following table for INA|INB configurations:
INA | INB | Function
 1  |  1  | Brake to Vcc
 1  |  0  | CW
 0  |  1  | CCW
 0  |  0  | Brake to GND
"""


# All wheels go forward; CW or CCW depends on left or right side.
def drive_forward():
    # left side goes clockwise
    # right side goes counter clockwise
    on = [
        p.INA2, # left side
        p.INA3,
        p.INB1, # right side
        p.INB4
    ]
    off = [
        p.INB2, # left side
        p.INB3,
        p.INA1, # right side
        p.INA4
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)

# All wheels go backward; CW or CCW depends on left or right side.
def drive_backward():
    # left side goes counter clockwise
    # right side goes clockwise
    off = [
        p.INA2, # left side
        p.INA3,
        p.INB1, # right side
        p.INB4
    ]
    on = [
        p.INB2, # left side
        p.INB3,
        p.INA1, # right side
        p.INA4
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)

# Base moves to the right until stopped.
def drive_right():
    on = [
        p.INA1, # front side
        p.INA2,
        p.INB3, # back side
        p.INB4
    ]
    off = [
        p.INB1, # front side
        p.INB2,
        p.INA3, # back side
        p.INA4
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)

# Base moves to the left until stopped.
def drive_left():
    off = [
        p.INA1, # front side
        p.INA2,
        p.INB3, # back side
        p.INB4
    ]
    on = [
        p.INB1, # front side
        p.INB2,
        p.INA3, # back side
        p.INA4
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)

# TODO: implement the following: (see braking to GND in truth table for wheels that don't move.)
# def drive_forward_left():
# def drive_forward_right():
# def drive_backward_left():
# def drive_backward_right():

# stops movement of motors by braking to GND TODO: determine whether braking to VCC is better
def stop():
    GPIO.output(chan_list, GPIO.LOW)



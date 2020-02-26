"""
This file contains the interface for driving the VNH5019A-E motor driver.
Filename: motor_controller.py
Author: Matthew Yu
Last Modified: 2/21/20
Notes:
    * How a Mecanum Drive Works: https://seamonsters-2605.github.io/archive/mecanum/
    * Driving a PWM pin in RPi.GPIO: https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
    * Motor Driver data sheet and logic table: https://www.pololu.com/file/0J504/vnh5019.pdf
    * RPI4 R5 Moving Base Pinout: https://docs.google.com/spreadsheets/d/1HRyUoHULSqokP9kBjE0gk1rphJi5dLCR_PKfli7fx-g/edit#gid=1188077649
    * Proposed operation:
        setup()
        set_speed(duty)
        drive_forward(s)
        ...
        shutdown()

    See the following table for INA|INB configurations:
    INA | INB | Function
     1  |  1  | Brake to Vcc
     1  |  0  | CW
     0  |  1  | CCW
     0  |  0  | Brake to GND
"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import time
import pins as p
import config as c
import encoders as e
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try using sudo privileges.")

GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
GPIO.setwarnings(False) # disable warnings from other drivers configuring other pins

# list of channels touched by motor controller.
chan_list = [
    p.INA_FR,    # Motor Driver 1 (Front Right)
    p.INB_FR,
    p.INA_FL,    # Motor Driver 2 (Front Left)
    p.INB_FL,
    p.INA_BL,    # Motor Driver 3 (Back Left)
    p.INB_BL,
    p.INA_BR,    # Motor Driver 4 (Back Right)
    p.INB_BR
]
# other channels touched, but these are PWM channels
pwm_list = [
    p.PWM0_FR,
    p.PWM0_BL,
    p.PWM1_FL,
    p.PWM1_BR
]
# pwm instances to drive motor controllers
pwms = []

"""
GENERAL_PURPOSE_COMMANDS - used for state changes
"""
# sets up the GPIO pins used for the motor controllers.
def setup(freq):
    print("Setup Motor Controllers.")
    GPIO.setup(chan_list, GPIO.OUT) # set all touched pins to output mode
    GPIO.setup(pwm_list, GPIO.OUT)  # set all touched pins to output mode
    for pwm_chan in pwm_list:
        pwms.append(GPIO.PWM(pwm_chan, freq)) # set motor frequency
    for pwm in pwms:
        pwm.start(0.0) # set default duty cycle to 0.0

# cleans all channels touched by motor controller
def shutdown():
    print("Shutdown Motor Controllers.")
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup(chan_list)
    GPIO.cleanup(pwm_list)

# sets the speed of the motors when enabled.
def set_speed(duty):
    for pwm in pwms:
        pwm.ChangeDutyCycle(duty)

"""
DRIVE_COMMANDS - move based on input time
"""
# Base moves forward until s seconds have passed.
def drive_forward(s):
    # left side goes clockwise
    # right side goes counter clockwise
    on = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    off = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves backward until s seconds have passed.
def drive_backward(s):
    # left side goes counter clockwise
    # right side goes clockwise
    off = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    on = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves to the right until s seconds have passed.
def drive_right(s):
    on = [
        p.INA_FR, # front side
        p.INA_FL,
        p.INB_BL, # back side
        p.INB_BR
    ]
    off = [
        p.INB_FR, # front side
        p.INB_FL,
        p.INA_BL, # back side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves to the left until s seconds have passed.
def drive_left(s):
    off = [
        p.INA_FR, # front side
        p.INA_FL,
        p.INB_BL, # back side
        p.INB_BR
    ]
    on = [
        p.INB_FR, # front side
        p.INB_FL,
        p.INA_BL, # back side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves forward left until s seconds have passed.
def drive_forward_left(s):
    on = [
        p.INB_FR,
        p.INA_BL
    ]
    off = [
        p.INA_FR,
        p.INA_FL,
        p.INB_FL,
        p.INB_BL,
        p.INA_BR,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves forward right until s seconds have passed.
def drive_forward_right(s):
    on = [
        p.INA_FL,
        p.INB_BR
    ]
    off = [
        p.INA_FR,
        p.INB_FR,
        p.INB_FL,
        p.INA_BL,
        p.INB_BL,
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves backward left until s seconds have passed.
def drive_backward_left(s):
    on = [
        p.INB_FL,
        p.INA_BR
    ]
    off = [
        p.INA_FR,
        p.INB_FR,
        p.INA_FL,
        p.INA_BL,
        p.INB_BL,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base moves backward right until s seconds have passed.
def drive_backward_right(s):
    on = [
        p.INA_FR,
        p.INB_BL
    ]
    off = [
        p.INB_FR,
        p.INA_FL,
        p.INB_FL,
        p.INA_BL,
        p.INA_BR,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base rotates left until s seconds have passed.
def drive_rotate_left(s):
    # all wheels go CCW
    on = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    off = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# Base rotates right until s seconds have passed.
def drive_rotate_right(s):
    # all wheels go CW
    on = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    off = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    time.sleep(s)
    stop()

# stops movement of motors by braking to GND
def stop():
    GPIO.output(chan_list, GPIO.LOW)

"""
DRIVE_COMMANDS_T - move based on encoder ticks
Notes:
 * these methods will clear ENCx_count for you
 * BIG assumption here that encoder ticks are consistent for each motor and are synchronous across all motors - verify this!
 * these methods are BLOCKING! Consider a multiprocessing approach: start a subprocess for each movement.
"""
# All wheels go forward until d ticks have passed
# d in ticks,
def drive_forward_t(d):
    # left side goes clockwise
    # right side goes counter clockwise
    on = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    off = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# All wheels go backward until d ticks have passed.
def drive_backward_t(d):
    # left side goes counter clockwise
    # right side goes clockwise
    off = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    on = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves to the right until d ticks have passed.
def drive_right_t(d):
    on = [
        p.INA_FR, # front side
        p.INA_FL,
        p.INB_BL, # back side
        p.INB_BR
    ]
    off = [
        p.INB_FR, # front side
        p.INB_FL,
        p.INA_BL, # back side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves to the left until d ticks have passed.
def drive_left_t(d):
    off = [
        p.INA_FR, # front side
        p.INA_FL,
        p.INB_BL, # back side
        p.INB_BR
    ]
    on = [
        p.INB_FR, # front side
        p.INB_FL,
        p.INA_BL, # back side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves forward left until d ticks have passed.
def drive_forward_left_t(d):
    on = [
        p.INB_FR,
        p.INA_BL
    ]
    off = [
        p.INA_FR,
        p.INA_FL,
        p.INB_FL,
        p.INB_BL,
        p.INA_BR,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves forward right until d ticks have passed.
def drive_forward_right_t(d):
    on = [
        p.INA_FL,
        p.INB_BR
    ]
    off = [
        p.INA_FR,
        p.INB_FR,
        p.INB_FL,
        p.INA_BL,
        p.INB_BL,
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves backward left until d ticks have passed.
def drive_backward_left_t(d):
    on = [
        p.INB_FL,
        p.INA_BR
    ]
    off = [
        p.INA_FR,
        p.INB_FR,
        p.INA_FL,
        p.INA_BL,
        p.INB_BL,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base moves backward right until d ticks have passed.
def drive_backward_right_t(d):
    on = [
        p.INA_FR,
        p.INB_BL
    ]
    off = [
        p.INB_FR,
        p.INA_FL,
        p.INB_FL,
        p.INA_BL,
        p.INA_BR,
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base rotates left until d ticks have passed.
def drive_rotate_left_t(d):
    # all wheels go CCW
    on = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    off = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# Base rotates right until d ticks have passed.
def drive_rotate_right_t(d):
    # all wheels go CW
    on = [
        p.INA_FL, # left side
        p.INA_BL,
        p.INA_FR, # right side
        p.INA_BR
    ]
    off = [
        p.INB_FL, # left side
        p.INB_BL,
        p.INB_FR, # right side
        p.INB_BR
    ]
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(off, GPIO.LOW)
    target = c.TICKS_PER_CM*d # TODO: this value should change based on independent experiments.
    # poll until the avg ticks of all motors reaches expected tick count
    while(getAvgTicks() < target):
        pass
    stop_t()

# stops movement of motors by braking to GND
def stop_t():
    for i in range(4):
        e.reset(i)
    GPIO.output(chan_list, GPIO.LOW)

# assuming we only move in cardinal and extracardinal ways
def getAvgTicks():
    return (c.ENC1_count + c.ENC2_count + c.ENC3_count + c.ENC4_count) / 4

def getAvgTicksRotate(mode):
    if(mode is 0): # rotate right, TODO: x and x motors are stationary
        pass
    elif(mode is 1):
        pass
    else:
        print("Invalid rotation mode: " + str(mode))

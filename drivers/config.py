"""
This file contains the global definitions of all variables used in the main program.
Filename: config.py
Author: Matthew Yu
Last Modified: 3/08/20
Usage:
    import config
    config.emergency_stop = False (stop_button.py)
"""
TICKS_PER_CM = 51.98 # see encoders.py, based on a 50mm. radius wheel and 16 ticks per revolution.
TICKS_SCALE = .5
TICKS_OFFSET = 10.6


MOTOR_PWM_FREQ=250
MOTOR_PWM_DUTY=80.0

FRONT_RIGHT=1
FRONT_LEFT=2
BACK_LEFT=3
BACK_RIGHT=4

ENC_FR_count = 0
ENC_FL_count = 0
ENC_BL_count = 0
ENC_BR_count = 0

emergency_stop = False      # determines whether the robot is in operation or halted.
lock = False

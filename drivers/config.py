"""
This file contains the global definitions of all variables used in the main program.
Filename: config.py
Author: Matthew Yu
Last Modified: 2/26/20
Usage:
    import config
    config.emergency_stop = False (stop_button.py)
"""
TICKS_PER_CM = 53 # see encoders.py, based on a 50mm. radius wheel and 64 ticks per revolution.

MOTOR_PWM_FREQ=100 # change these
MOTOR_PWM_DUTY=10.0

FRONT_RIGHT=1
FRONT_LEFT=2
BACK_LEFT=3
BACK_RIGHT=4

emergency_stop = False      # determines whether the robot is in operation or halted.
ENC_FR_count = 0
ENC_FL_count = 0
ENC_BL_count = 0
ENC_BR_count = 0

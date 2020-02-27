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

emergency_stop = False      # determines whether the robot is in operation or halted.
ENC1_count = 0
ENC2_count = 0
ENC3_count = 0
ENC4_count = 0

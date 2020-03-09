"""
This file contains the global definitions of all used pins on the RPI4.
All pins are labeled by GPIO number. 
Filename: pins.py
Author: Matthew Yu
Last Modified: 2/15/20
Usage: 
    import pins as *
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
"""


"""
There are four motors and motor drivers. The (n) corresponds to each motor position
    (1) Front Right
    (2) Front Left
    (3) Back Left
    (4) Back Right
"""

"""
Motor Drivers
INA, INB pins controls motor directionality.
Truth table:
INA | INB | MODE
 1  |  1  | Brake to Vcc
 1  |  0  | Clockwise
 0  |  1  | Counterclockwise
 0  |  0  | Brake to GND
"""
INA_FR = 14      # IN A port on Motor Driver (1). 
INB_FR = 15      # IN B port on Motor Driver (1)
INA_FL = 26      # IN A port on Motor Driver (2)
INB_FL = 16      # IN B port on Motor Driver (2)
INA_BL = 23      # IN A port on Motor Driver (3)
INB_BL = 24      # IN B port on Motor Driver (3)
INA_BR = 20      # IN A port on Motor Driver (4)
INB_BR = 21      # IN B port on Motor Driver (4)
"""
PWM pins
"""
PWM0_FR = 18
PWM1_FL = 13
PWM0_BL = 12
PWM1_BR = 19

"""
Encoder pins
"""
ENC_FR = 2
ENC_FL = 3
ENC_BL = 17
ENC_BR = 27

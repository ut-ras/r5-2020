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
INA1 = 14      # IN A port on Motor Driver (1). 
INB1 = 15      # IN B port on Motor Driver (1)
INA2 = 26      # IN A port on Motor Driver (2)
INB2 = 16      # IN B port on Motor Driver (2)
INA3 = 23      # IN A port on Motor Driver (3)
INB3 = 24      # IN B port on Motor Driver (3)
INA4 = 20      # IN A port on Motor Driver (4)
INB4 = 21      # IN B port on Motor Driver (4)
"""
PWM pins
"""
PWM0_1 = 18     # Motor Driver  (1)
PWM0_3 = 12     # Motor Driver  (3)
PWM1_2 = 13     # Motor Driver  (2)
PWM1_4 = 19     # Motor Driver  (4)
"""
Servo Motor
"""
SERV0 = 25      # servo motor software defined PWM pin for the bin
"""
Motor MOSFETs
"""
M_DRUM = 17     # logic signal to the MOSFET enabling the drum motor.
M_BELT = 27     # logic signal to the MOSFET enabling the conveyor belt motor.
"""
Emergency Stop Switch
"""
STOP_SW = 22    # When raised high, an interrupt stops all threads and polls until lowered again.
"""
Bonnet Pins
"""
BON_1 = 2       # TODO: define at a later time.
BON_2 = 3

"""
Encoder pins - TODO: subject to change for final pinout.
"""
AOUT1 = 2       # Encoder AOUT (1)
BOUT1 = 3       # Encoder BOUT (1)
AOUT2 = 4       # Encoder AOUT (2)
BOUT2 = 17      # Encoder BOUT (2)
AOUT3 = 27      # Encoder AOUT (3)
BOUT3 = 22      # Encoder BOUT (3)
AOUT4 = 10      # Encoder AOUT (4)
BOUT4 = 9       # Encoder BOUT (4)

"""
Ultrasonic Sensor pins - TODO: subject to change for final pinout.
"""
ECHO_1 = 0      # TODO: define at a later time.
TRIG_1 = 0
ECHO_2 = 0
TRIG_2 = 0
ECHO_3 = 0
TRIG_3 = 0
ECHO_4 = 0
TRIG_4 = 0
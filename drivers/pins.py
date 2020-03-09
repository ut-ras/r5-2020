"""
This file contains the global definitions of all used pins on the RPI4.
All pins are labeled by GPIO number. 
Filename: pins.py
Author: Matthew Yu
Last Modified: 03/08/20
Usage: 
    import pins
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM) # pin values correspond to GPIO pin number on board
    pin_a = pins.INA_FR
"""

"""
MOTOR SYSTEM
Motor Drivers
INA, INB pins controls motor directionality.
Truth table:
INA | INB | MODE
 1  |  1  | Brake to Vcc
 1  |  0  | Clockwise
 0  |  1  | Counterclockwise
 0  |  0  | Brake to GND
"""
INA_FR = 14      # IN A port on Motor Driver 
INB_FR = 15      # IN B port on Motor Driver
INA_FL = 26      # IN A port on Motor Driver
INB_FL = 16      # IN B port on Motor Driver
INA_BL = 23      # IN A port on Motor Driver
INB_BL = 24      # IN B port on Motor Driver
INA_BR = 20      # IN A port on Motor Driver
INB_BR = 21      # IN B port on Motor Driver
"""
PWM pins
"""
PWM0_FR = 18     # Motor Driver  (1)
PWM1_FL = 13     # Motor Driver  (2)
PWM0_BL = 12     # Motor Driver  (3)
PWM1_BR = 19     # Motor Driver  (4)
"""
Encoder pins
"""
ENC_FR = 9
ENC_FL = 11
ENC_BL = 5
ENC_BR = 6


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
Servo Motor
"""
SERV0 = 25      # servo motor software defined PWM pin for the bin


"""
Bonnet Pins
"""
BON_SDA = 2
BON_SCL = 3
"""
Ultrasonic Sensor pins - TODO: subject to change for final pinout.
"""
ECHO_1 = 0      # TODO: define at a later time for GPIO bonnet extender.
TRIG_1 = 0
ECHO_2 = 0
TRIG_2 = 0
ECHO_3 = 0
TRIG_3 = 0
ECHO_4 = 0
TRIG_4 = 0
"""
IMU
"""
IMU_SDA = 2
IMU_SCL = 3
RST = 0   # TODO: define at a later time for GPIO bonnet extender
INT = 0
ADR = 0

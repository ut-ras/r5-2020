"""
This file tests the interface for driving both motors and encoders.
Filename: test_motor_system.py
Author: Matthew Yu
Last Modified: 2/21/20
"""
import sys
sys.path.append("../encoders/")
sys.path.append("../motor_controller/")

import time as t
import encoders as e
import motor_controller as m
import config



# setup motor controller and encoders
e.setup()
m.setup(config.MOTOR_PWM_FREQ)
m.set_speed(config.MOTOR_PWM_DUTY)

# drive forward
m.drive_forward(5) # 5 seconds
print("Ticks: " + str(e.read(1))) # reading from encoder 1 (Front Right)

# reset count
e.reset(1)
print("Ticks: " + str(e.read(1))) # should be reading 0 now

# drive backward
m.drive_backward(5)
print("Ticks: " + str(e.read(1)))

# shutdown
e.shutdown()
m.shutdown()

"""
This file tests the interface for driving both motors and encoders.
Filename: test_motor_system.py
Author: Matthew Yu
Last Modified: 2/21/20
"""
from .. import encoders as e
from .. import motor_controller as m

MOTOR_PWM_FREQ=100 # change these
MOTOR_PWM_DUTY=10.0

# setup motor controller and encoders
e.setup()
m.setup(MOTOR_PWM_FREQ)
m.set_speed(MOTOR_PWM_DUTY)

# drive forward
m.drive_forward(5) # 5 seconds
e.read(1) # reading from encoder 1 (Front Right)

# reset count
e.reset(1)
e.read(1) # should be reading 0 now

# drive backward
m.drive_backward(5)
e.read(1)

# shutdown
e.shutdown()
m.shutdown()

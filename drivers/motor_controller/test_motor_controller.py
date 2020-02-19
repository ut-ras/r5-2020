"""
This file tests the interface for driving the VNH5019A-E motor driver.
Filename: test_motor_controller.py
Author: Matthew Yu
Last Modified: 2/19/20
Notes: 
    * Proposed operation:
        setup()
        set_speed(duty)
        drive_forward(ms)
        ...
        shutdown()

"""
import motor_controller as m

MOTOR_PWM_FREQ=100 # change these
MOTOR_PWM_DUTY=1.0

m.setup(MOTOR_PWM_FREQ)
m.set_speed(MOTOR_PWM_DUTY)
m.drive_forward(1)
m.drive_backward(1)
# add more commands here
m.shutdown()
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
MOTOR_PWM_DUTY=10.0

m.setup(MOTOR_PWM_FREQ)
# Test regime:
for i in range(0, 10):
    m.set_speed(MOTOR_PWM_DUTY*i)
    m.drive_forward(5)
# m.drive_backward(10)
# add more commands here
m.shutdown()

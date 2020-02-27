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
import motor_controller
import config

m.setup(config.MOTOR_PWM_FREQ)
# Test regime:
#for i in range(0, 10):
#    m.set_speed(MOTOR_PWM_DUTY*i)
#    m.drive_forward(5)
m.set_speed(config.MOTOR_PWM_DUTY)
m.drive_backward(5)

# m.drive_backward(10)
# add more commands here
m.shutdown()

"""
This file tests the interface for driving both motors and encoders.
Filename: test_motor_system.py
Author: Matthew Yu
Last Modified: 2/21/20
"""
import sys
sys.path.append("../encoders/")
sys.path.append("../motor_controller/")

import time
import numpy as np
import encoders
import motor_controller
import config

# setup motor controller and encoders
encoders.setup()
motor_controller.setup(config.MOTOR_PWM_FREQ)
motor_controller.set_speed(config.MOTOR_PWM_DUTY)

try:
	# drive forward
	motor_controller.drive_forward_t(3)
#	time.sleep(1)
	# drive backward
	motor_controller.drive_backward_t(3)
#	time.sleep(1)
	# drive left
	motor_controller.drive_right_t(3)
#	time.sleep(1)
	# drive right
	motor_controller.drive_left_t(3)
#	time.sleep(1)
	# drive forward left
	motor_controller.drive_forward_left_t(3)
	# drive forward right
	motor_controller.drive_forward_right_t(3)
	# drive backward left
	motor_controller.drive_backward_left_t(3)
	# drive backward right
	motor_controller.drive_backward_right_t(3)
	# shutdown
	encoders.shutdown()
	motor_controller.shutdown()

except KeyboardInterrupt:
	encoders.shutdown()
	motor_controller.shutdown()

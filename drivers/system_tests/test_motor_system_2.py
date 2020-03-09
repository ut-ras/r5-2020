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
import numpy as np
import encoders
import motor_controller
import config

# setup motor controller and encoders
encoders.setup()

motor_controller.setup(config.MOTOR_PWM_FREQ)

try:
    motor_controller.set_speed(config.MOTOR_PWM_DUTY)
    # up freq and repeat
    for f in range(0,2): # 1-10
        # modify encoder ticks
        enc_ticks = f * 100
        # drive forward
        print("Moving forward " + str(enc_ticks) + " ticks.")

        for run in range(0, 6):
            while config.lock is True:
                print("Waiting for motor controller to free up lock.")
            motor_controller.drive_forward_t(enc_ticks)
            res = input("Press enter to continue.")

    # shutdown
    encoders.shutdown()
    motor_controller.shutdown()
except KeyboardInterrupt:
    encoders.shutdown()
    motor_controller.shutdown()

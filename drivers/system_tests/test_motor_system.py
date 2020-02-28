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
import encoders
import motor_controller
import config

# setup motor controller and encoders
encoders.setup()

freq = []

# up freq and repeat
for f in range(1,11): # 1-10
    # modify freq
    motor_controller.setup(config.MOTOR_PWM_FREQ*f)
    
    duty = []
    # up duty and repeat
    for d in range(11): # 0-10
        # modify power
        motor_controller.set_speed(config.MOTOR_PWM_DUTY*d)
        
        for i in range(5): # repeat trial 5 times
            # drive forward
            motor_controller.drive_forward(.5) # 1 second
            print("Ticks: " + str(encoders.read(config.FRONT_LEFT))) # reading from encoder Back Right

            # append to dataset
            duty.append(
                [config.MOTOR_PWM_DUTY*d, encoders.read(config.FRONT_LEFT)]
                )
            # reset ticks
            encoders.reset(config.FRONT_LEFT)
    
    # append to dataset
    freq.append(
        [config.MOTOR_PWM_FREQ*f, duty]
        )

    # restart motor controller
    motor_controller.shutdown()

# display result
for freqEntry in freq:
    for dutyEntry in freqEntry[1]:
        for entry in dutyEntry[1]:
            print(freqEntry[0] + "\t|\t" + dutyEntry[0] + "\t|\t" + entry)


# shutdown
encoders.shutdown()
# motor_controller.shutdown()

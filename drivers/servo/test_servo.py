"""
This file tests the interface for driving the HD-1501MG stepper motor.
Filename: test_servo.py
Author: Matthew Yu
Last Modified: 2/21/20
Notes: 
    * Proposed operation:
        setup()
        extend()
        rest()
        shutdown()

"""
import servo as s
import time


s.setup()
s.extend()
time.sleep(3)
s.rest()
s.shutdown()
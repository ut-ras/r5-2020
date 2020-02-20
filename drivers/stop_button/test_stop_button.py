"""
This file tests the interface for driving the emergency stop button, placed on the top of the robot.
Filename: test_stop_button.py
Author: Matthew Yu
Last Modified: 2/20/20
Notes:
    * Proposed operation:
        setup()
        ...
        shutdown()
"""
import stop_button as s
import config as c

s.setup()
while(c.emergency_stop is False):
    print("Waiting for button press.")

print("Button is pressed! Shutting down.")
s.shutdown()
"""
This file tests the interface for driving the motor encoders.
Filename: test_encoders.py
Author: Matthew Yu
Last Modified: 2/21/20
Notes:
    * Proposed operation:
        setup()
        ...
        shutdown()
"""
import encoders as e

e.setup()
input = input("Press enter to quit\n\n")
e.read(0) # should return an error message
e.read(1) # should return 0 since motor isn't moving.
e.reset(0) # should return an error message
e.reset(1) # should work. Read should be 0 now if it wasn't already.
e.read(1)
e.shutdown()

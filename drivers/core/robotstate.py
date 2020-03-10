from enum import Enum

# actuator states
class BinServoState(Enum):
	REST = 0
	DUMP = 1


class DrumMotorState(Enum):
	OFF = 0
	ON = 1


class ConveyorMotorState(Enum):
	OFF = 0
	ON = 1


# state of execution
class ProgramMode(Enum):
	PAUSED = 0
	SEARCHING = 1
	PICKING_UP = 2
	DEPOSITING = 3
	END = 4

"""
	Additional state considerations
		1. Current expected position of robot
		2. Bin status: how many items we think we collected
		3. Waypoints
		4. Target velocity
"""


class RobotState:
	"""
	Represents the state of the robot at a point in time
	"""
	pass
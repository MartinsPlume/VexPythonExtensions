from vex import *

class DriveTrainExtended(DriveTrain):
    def __init__(self, lm, rm, wheelTravel=300, trackWidth=320, wheelBase=320,
                 units=DistanceUnits.MM, externalGearRatio=1.0):
        super().__init__(lm, rm, wheelTravel, trackWidth, wheelBase, units, externalGearRatio)

    def turn_slightly(self, direction, speed):
        if direction == TurnType.LEFT:
            self.lm.spin(FORWARD, 100 - speed, PERCENT)
            self.rm.spin(FORWARD)
        elif direction == TurnType.RIGHT:
            self.rm.spin(FORWARD, 100 - speed, PERCENT)
            self.lm.spin(FORWARD)
    
class SmartDriveExtended(SmartDrive):
    def __init__(self, lm, rm, g, wheelTravel=300, trackWidth=320, wheelBase=320,
                 units=DistanceUnits.MM, externalGearRatio=1.0):
        super().__init__(lm, rm, g, wheelTravel, trackWidth, wheelBase, units, externalGearRatio)

    def turn_slightly(self, direction, speed):
        if direction == TurnType.LEFT:
            self.lm.spin(FORWARD, 100 - speed, PERCENT)
            self.rm.spin(FORWARD)
        elif direction == TurnType.RIGHT:
            self.rm.spin(FORWARD, 100 - speed, PERCENT)
            self.lm.spin(FORWARD)
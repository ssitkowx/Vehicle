from enum import IntEnum, unique

class Settings:
    @unique
    class EMoveDirection (IntEnum):
        Forward  = 0,
        Backward = 1,
        Left     = 2,
        Right    = 3,
        Stop     = 4
    
    @unique
    class EChannel (IntEnum):
        One = 1
        Two = 2

    #class ImuAngles:
    #    X = 0
    #    Y = 0
    #    Z = 0

    class DutyParams:
        RANGE = { "Top"    : 1.0,
                  "Bottom" : -1.0
                }
        STEP           = 0.1
        FACTOR         = 1.0
        TO_SPEED_COEFF = 100
    
    ADDRESS   = "98:84:E3:E0:A6:92"
    UUID      = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    
    duty      = 0.0
    brake     = False
    freeSpin  = False
    direction = EMoveDirection.Stop
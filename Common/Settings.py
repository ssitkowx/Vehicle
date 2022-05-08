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
    
    DUTY_RANGE          = { "Top"    : 1,
                            "Bottom" : -1
                          }
    DUTY_STEP           = 0.05
    DUTY_TO_SPEED_COEFF = 100
    
    MOTORS              = { "LeftWheel"  : EChannel.One,
                            "RightWheel" : EChannel.Two
                          }
    direction           = EMoveDirection.Stop
    ADDRESS             = {}
    UUID                = "94f39d29-7d6d-437d-973b-fba39e49d4ee"


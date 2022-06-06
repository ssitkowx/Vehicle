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
    
    DUTY_RANGE          = { "Top"    : 10,
                            "Bottom" : -10
                          }
    DUTY_STEP           = 1
    DUTY_FACTOR         = 10
    DUTY_TO_SPEED_COEFF = 100
    ADDRESS             = "98:84:E3:E0:A6:92"
    UUID                = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    
    duty                = 0
    brake               = False
    freeSpin            = False
    direction           = EMoveDirection.Stop
    acceleroemterX      = 0
    acceleroemterY      = 0
    acceleroemterZ      = 0
    
    


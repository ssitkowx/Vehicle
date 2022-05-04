from enum import Enum, unique

class Settings:
    @unique
    class EDirection (Enum):
        eForward  = 0,
        eBackward = 1,
        eLeft     = 2,
        eRight    = 3,
        eStop     = 4
        
    UUID      = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    ADDRESS   = {}
    speed     = 0
    direction = EDirection.eStop
    
    motors    = { "LeftWheel"  : [{ "Duty" : 0 }, { "Brake" : False }, { "FreeSpin" : True }],
                  "RightWheel" : [{ "Duty" : 0 }, { "Brake" : False }, { "FreeSpin" : True }]
                }

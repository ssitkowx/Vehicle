from enum import Enum, unique

class Settings:
    @unique
    class EDirection (Enum):
        eLeft     = 0,
        eStop     = 1,
        eRight    = 2,
        eForward  = 3,
        eBackward = 4
    
    UUID    = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    ADDRESS = {}
    
    def __init__ (self):
        self.direction = self.EDirection.eStop
        self.speed     = 0

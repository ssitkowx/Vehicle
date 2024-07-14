import Cmd_pb2 as CmdProto
from enum import IntEnum, unique

class Settings:
    ADDRESS = "98:84:E3:E0:A6:92"
    UUID    = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    def __init__ (self):
        self.imuAnglesMsg       = CmdProto.ImuAngles ()
        self.imuAnglesMsg.Roll  = 0
        self.imuAnglesMsg.Pitch = 0
        self.imuAnglesMsg.Yaw   = 0
        
        self.vehicleMsg           = CmdProto.Vehicle ()
        self.vehicleMsg.Duty      = 0
        self.vehicleMsg.Direction = CmdProto.EDirection.Stop
    
    @unique
    class EChannel (IntEnum):
        One = 0
        Two = 1
    
    class Duty:
        RANGE = { "Top"    : 1.0,
                  "Bottom" : -1.0
                }
        TIMEOUT = 100

    brake     = False
    freeSpin  = False
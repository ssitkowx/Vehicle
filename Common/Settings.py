import Cmd_pb2 as CmdProto
from enum import IntEnum, unique

class Settings:
    ADDRESS = "98:84:E3:E0:A6:92"
    UUID    = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    def __init__ (self):
        self.imuAnglesMsg         = CmdProto.ImuAngles ()
        self.imuAnglesMsg.Roll    = 0
        self.imuAnglesMsg.Pitch   = 0
        self.imuAnglesMsg.Yaw     = 0
        self.vehicleMsg           = CmdProto.Vehicle ()
        self.vehicleMsg.Duty      = 0
        self.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index
    
    @unique
    class EChannel (IntEnum):
        One = 0
        Two = 1
    
    class Duty:
        STEP  = 5
        RANGE = { "Top"    : 100,
                  "Bottom" : -100
                }
        TIMEOUT  = 100
        DEV_COEF = RANGE ["Top"]

    brake     = False
    freeSpin  = False
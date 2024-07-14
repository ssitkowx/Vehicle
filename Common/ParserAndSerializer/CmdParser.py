import Cmd_pb2 as CmdProto

from   Logger   import *
from   Settings import Settings

class CmdParser:
    module = __name__

    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def parse (self, vMsg):
        msg = CmdProto.Msg ()
        msg.ParseFromString (vMsg)
    
        if   msg.HasField ("Vehicle")  : self.__cmd       (msg.Vehicle)
        elif msg.HasField ("ImuAngles"): self.__imuAngles (msg.ImuAngles)
        else                           : LOGE (self.module, "Unhandled message")
    
    def __cmd (self, vMsg):
        self.settings.vehicleMsg.Duty      = vMsg.Duty
        self.settings.vehicleMsg.Direction = vMsg.Direction

    def __imuAngles (self, vMsg):
        self.settings.imuAnglesMsg.Roll  = vMsg.Roll
        self.settings.imuAnglesMsg.Pitch = vMsg.Pitch
        self.settings.imuAnglesMsg.Yaw   = vMsg.Yaw
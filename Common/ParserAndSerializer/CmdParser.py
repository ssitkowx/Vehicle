import Cmd_pb2 as CmdProto
from Settings import Settings

class CmdParser:
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def parse (self, vMsg):
        msg = CmdProto.Vehicle ()
        msg.ParseFromString (vMsg)
        self.settings.vehicleMsg.Duty      = msg.Duty
        self.settings.vehicleMsg.Direction = msg.Direction
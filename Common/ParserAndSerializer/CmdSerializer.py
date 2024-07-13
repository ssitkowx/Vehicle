import Cmd_pb2 as CmdProto
from Settings import Settings

class CmdSerializer:
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def serialize (self):
        msg = CmdProto.Vehicle ()
        if self.settings.vehicleMsg.Duty is not None:
            msg.Duty = self.settings.vehicleMsg.Duty
        msg.Direction = self.settings.vehicleMsg.Direction
        return msg.SerializeToString ()
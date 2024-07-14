import Cmd_pb2 as CmdProto
from Settings import Settings

class CmdSerializer:
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def cmd (self):
        msg = CmdProto.Msg ()
        if self.settings.vehicleMsg.Duty is not None:
            msg.Vehicle.Duty = self.settings.vehicleMsg.Duty
        msg.Vehicle.Direction = self.settings.vehicleMsg.Direction
        return msg.SerializeToString ()
    
    def imu (self):
        msg = CmdProto.Msg ()
        if self.settings.imuAnglesMsg.Roll is not None:
            msg.ImuAngles.Roll = self.settings.imuAnglesMsg.Roll

        if self.settings.imuAnglesMsg.Pitch is not None:
            msg.ImuAngles.Pitch = self.settings.imuAnglesMsg.Pitch

        if self.settings.imuAnglesMsg.Yaw is not None:
            msg.ImuAngles.Yaw = self.settings.imuAnglesMsg.Yaw
        return msg.SerializeToString ()
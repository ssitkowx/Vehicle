from Settings import Settings

class CommandConverter:
    def __init__ (self, vSettings: Settings):
        self.settings = vSettings
    
    def convert (self, vCommand: str):
        if vCommand == "Move":
            self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index
        elif vCommand == "Turn left":
            self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Left'].index
        elif vCommand == "Turn right":
            self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Right'].index
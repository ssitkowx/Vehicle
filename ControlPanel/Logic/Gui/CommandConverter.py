from Settings import Settings

class CommandConverter:
    def __init__ (self, vSettings: Settings):
        self.settings = vSettings
    
    def convert (self, vCommand: str):
        if vCommand == "Move forward":
            self.settings.direction = self.settings.EMoveDirection.Forward
        elif vCommand == "Move backward":
            self.settings.direction = self.settings.EMoveDirection.Backward
        elif vCommand == "Turn left":
            self.settings.direction = self.settings.EMoveDirection.Left
        elif vCommand == "Turn right":
            self.settings.direction = self.settings.EMoveDirection.Right
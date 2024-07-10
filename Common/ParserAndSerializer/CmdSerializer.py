import json
from   Settings import Settings

class CmdSerializer:
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def serialize (self):
        msg = { "Duty"          : self.settings.Duty.data,
                "MoveDirection" : self.settings.direction
              }
        return json.dumps (msg)
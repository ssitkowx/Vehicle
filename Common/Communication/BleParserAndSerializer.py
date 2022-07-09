import json
from   Settings import Settings

class BleParserAndSerializer:
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.settings = vSettings
    
    def parse (self, vMsg):
        jsonMsg                 = json.loads (vMsg)
        self.settings.direction = jsonMsg ["MoveDirection"]
    
    def serialize (self):
        msg = { "MoveDirection" : self.settings.direction }
        return json.dumps (msg)
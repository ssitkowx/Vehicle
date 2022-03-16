import json
from   Settings import Settings

class BleParserAndSerializer:
    def __init__ (self, vSettings: Settings):
        self.settings = vSettings
    
    def parse (self, vMsg):
        jsonMsg                 = json.loads (vMsg)
        self.settings.speed     = jsonMsg ["Speed"]
        self.settings.direction = jsonMsg ["Direction"]
    
    def serialize (self):
        msg = {'Direction' : str (self.settings.direction,),
               'Speed'     : self.settings.speed }
        return json.dumps (msg)
'''
if __name__ == '__main__':
    settings                   = Settings                   ()
    vehicleParserAndSerializer = VehicleParserAndSerializer (settings)
    jsonMsg = vehicleParserAndSerializer.serialize ()
    print (jsonMsg)
    vehicleParserAndSerializer.parse (jsonMsg)
    print (f"speed: {settings.speed}, direction: {settings.direction}")
'''
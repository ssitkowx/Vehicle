from Rtos                   import Rtos
from pynput                 import keyboard
from Settings               import Settings
from BleParserAndSerializer import BleParserAndSerializer

class Keyboard:
    def __init__ (self, vRtos: Rtos, vSettings: Settings, vBleParserAndSerializer: BleParserAndSerializer):
        self.rtos                        = vRtos
        self.settings                    = vSettings
        self.bleParserAndSerializer      = vBleParserAndSerializer
        with keyboard.Listener (on_press = self.press) as listener: listener.join ()
        
    def press (self, vKey):
        try:
            if   vKey.name == 'left' : self.settings.direction = self.settings.EMoveDirection.Left
            elif vKey.name == 'right': self.settings.direction = self.settings.EMoveDirection.Right
            elif vKey.name == 'up'   : self.settings.direction = self.settings.EMoveDirection.Forward
            elif vKey.name == 'down' : self.settings.direction = self.settings.EMoveDirection.Backward
            else: pass
        except AttributeError:
            if vKey.char == 's': self.settings.direction = self.settings.EMoveDirection.Stop
            else: pass
        
        self.rtos.sendMsg (self.bleParserAndSerializer.serialize ())
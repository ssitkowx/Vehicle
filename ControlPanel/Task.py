from Paths                  import *
from Rtos                   import Rtos
from Logger                 import *
from Settings               import Settings
from Keyboard               import Keyboard
from BleClientComm          import BleClientComm
from BleParserAndSerializer import BleParserAndSerializer

class Task:
    def __init__ (self):
        self.rtos       = Rtos     ()
        self.settings   = Settings ()
        keyboardThread  = self.rtos.createThread (self.keyboardProcess)
        keyboardThread .start ()
        
        bleClientThread = self.rtos.createThread (self.bleClientProcess)
        bleClientThread.start ()
    
        keyboardThread .join  ()
        bleClientThread.join  ()
    
    def keyboardProcess (self):
        bleParserAndSerializer = BleParserAndSerializer (self.settings)
        keyboard               = Keyboard               (self.rtos, self.settings, bleParserAndSerializer)
        LOGI                                            ("Enter message")
    
    def bleClientProcess (self):
        bleClientComm = BleClientComm (self.settings)
    
        while True:
            try:
                msg = self.rtos.getMsg  ()
                LOGI                    (f"Send: { msg }")
                bleClientComm.sock.send (msg)
            except OSError:
                bleClientComm.sock.close ()
                LOGE                     ("bleClientProcess disconnected")

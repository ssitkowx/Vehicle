from   Paths                  import *
from   Rtos                   import Rtos
from   Logger                 import *
from   Settings               import Settings
from   BleServerComm          import BleServerComm
#from   BleParserAndSerializer import BleParserAndSerializer

class Task:
    def __init__ (self):
        self.rtos          = Rtos     ()
        self.settings      = Settings ()
        #controlPanelThread = self.rtos.createThread (self.keyboardProcess)
        #controlPanelThread.start ()
        
        bleClientThread    = self.rtos.createThread (self.bleServerProcess)
        bleClientThread   .start ()
    
        #controlPanelThread.join  ()
        bleClientThread   .join  ()
    
    def bleServerProcess (self):
        bleServerComm = BleServerComm ()
        
        try:
            while True:
                data = bleServerComm.clientSock.recv (1024)
                if not data:
                    break
            
                LOGI ("Received", data)
                # parse data or better add to queue
        except OSError:
                pass
            
        LOGE ("Disconnected.")

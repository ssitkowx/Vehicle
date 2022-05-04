from Paths                  import *
from App                    import App
from Rtos                   import Rtos
from Logger                 import *
from Settings               import Settings
from BleServerComm          import BleServerComm
from BleParserAndSerializer import BleParserAndSerializer

class Task:
    def __init__ (self):
        self.rtos                   = Rtos                   ()
        self.settings               = Settings               ()
        self.bleParserAndSerializer = BleParserAndSerializer (self.settings)
        
        self.bleServerThread = self.rtos.createThread (self.bleServerProcess)
        self.bleServerThread.start ()
        
        self.appThread       = self.rtos.createThread (self.appProcess)
        self.appThread      .start ()
    
        self.bleServerThread.join  ()
        self.appThread      .join  ()

    def bleServerProcess (self):
        BleServerComm ()
        
        try:
            while True:
                msg = self.bleServerThread.clientSock.recv (1024)
                if not msg:
                    break
                
                LOGI (f"Received: {msg}")
                self.rtos.sendMsg (msg)
        except OSError:
            pass
            
        LOGE ("Disconnected.")

    def appProcess (self):
        app = App (self.settings)
        
        try:
            while True:
                msg = self.rtos.getMsg ()
                self.bleParserAndSerializer.parse (msg)
                app.process ()
        except OSError:
                pass
        
        LOGE ("Disconnected.")
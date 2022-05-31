from Paths                  import *
from App                    import App
from Rtos                   import Rtos
from Logger                 import *
from Settings               import Settings
from BleServerComm          import BleServerComm
from BleParserAndSerializer import BleParserAndSerializer

class Task:
    rtos                   = Rtos                   ()
    settings               = Settings               ()
    app                    = App                    (settings)
    bleParserAndSerializer = BleParserAndSerializer (settings)
    
    def __init__ (self):
        self.bleServerThread = self.rtos.createThread (self.bleServerProcess)
        self.bleServerThread.start ()

        self.appThread       = self.rtos.createThread (self.appProcess)
        self.appThread      .start ()
    
        self.bleServerThread.join  ()
        self.appThread      .join  ()
        
    def isBleServerProcessRunning (self):
        return True

    def isAppProcessRunning (self): 
        return True
    
    def bleServerProcess (self):
        BleServerComm (self.settings)
        
        while self.isBleServerProcessRunning ():
            try:
                msg = self.bleServerThread.clientSock.recv (1024)
                if not msg:
                    break
                
                LOGI (f"Received: {msg}")
                self.rtos.sendMsg (msg)
            except OSError:
                LOGI ('My exception')
                pass
            
        LOGE ("bleServerProcess disconnected")

    def appProcess (self):  
        while self.isAppProcessRunning ():
            try:
                msg = self.rtos.getMsg ()
                self.bleParserAndSerializer.parse (msg)
                self.app.process ()
            except OSError:
                pass
        
        LOGE ("appProcess disconnected")
from   Paths                  import *
import time
from   App                    import App
from   Rtos                   import Rtos
from   Logger                 import *
from   Settings               import Settings
from   BleServerComm          import BleServerComm
from   BleParserAndSerializer import BleParserAndSerializer

class Task:
    rtos                   = Rtos                   ()
    settings               = Settings               ()
    app                    = App                    (settings)
    bleServerComm          = BleServerComm          (settings)
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
    
    def bleServerProcess (self):
        
        while self.isBleServerProcessRunning ():
            try:
                msg = self.bleServerComm.clientSock.recv (1024)
                if not msg:
                    break
                
                LOGI (f"Received: {msg}")
                self.rtos.sendMsg (msg)
            except OSError:
                LOGE ("appProcess disconnected")
                self.bleServerComm.clientSock.close ()
                self.bleServerComm.sock      .close ()

    def appProcess (self):  
        while self.app.isExiting () == False:
            try:
                if self.app.isRunning () == True:
                    msg = self.rtos.getMsg            ()
                    self.bleParserAndSerializer.parse (msg)
                    self.app.process                  ()
                    LOGE ("AAAAAAAAAAAAAAAAAAA")
                elif self.app.isPaused () == True:
                    self.settings.freeSpin = True
                    LOGE ("BBBBBBBBBBBBBBBBBBBBBB")

                time.sleep (0.3)

            except OSError:
                LOGE ("appProcess disconnected")

            finally:
                LOGE ("appProcess disconnected finally")
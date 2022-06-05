from   Paths                  import *
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
    bleParserAndSerializer = BleParserAndSerializer (settings)
    
    def __init__ (self):
        self.bleServerComm   = BleServerComm          (self.settings)
        self.bleServerThread = self.rtos.createThread (self.bleServerProcess)
        self.bleServerThread.start ()

        self.appThread       = self.rtos.createThread (self.appProcess)
        self.appThread      .start ()
    
        self.bleServerThread.join  ()
        self.appThread      .join  ()

    def isBleProcessRunning (self):
        return True
    
    def bleServerProcess (self):
        while self.isBleProcessRunning ():
            try:
                msg = self.bleServerComm.clientSock.recv (1024)
                if self.app.isMsgDoubled (msg.decode ('UTF-8')) == True:
                    continue

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
                    LOGI                              (f"Received: {msg}")
                    self.bleParserAndSerializer.parse (msg)
                    self.app.process                  ()
                elif self.app.isPaused () == True:
                    self.settings.freeSpin = True

            except OSError:
                LOGE ("appProcess disconnected")
import time
import Paths
from   App                    import App
from   Rtos                   import Rtos
from   Logger                 import *
from   BleComm                import BleComm
from   Settings               import Settings
from   Accelerometer          import Accelerometer
from   BleParserAndSerializer import BleParserAndSerializer

class Process:
    rtos                   = Rtos                   ()
    settings               = Settings               ()
    app                    = App                    (settings)
    bleParserAndSerializer = BleParserAndSerializer (settings)
    
    def __init__ (self):
        self.bleComm            = BleComm                (self.settings)
        self.accelerometer      = Accelerometer          (self.settings)
        self.bleServerThread    = self.rtos.createThread (self.bleServerProcess)
        self.bleServerThread    .start ()

        self.appThread           = self.rtos.createThread (self.appProcess)
        self.appThread          .start ()

        self.accelerometerThread = self.rtos.createThread (self.accelerometerProcess)
        self.accelerometerThread.start ()
    
        self.bleServerThread    .join  ()
        self.appThread          .join  ()
        self.accelerometerThread.join  ()

    def isBleProcessRunning (self):
        return True
    
    def bleServerProcess (self):
        while self.isBleProcessRunning ():
            try:
                msg = self.bleComm.clientSock.recv (1024)
                if self.app.isMsgDoubled (msg.decode ('UTF-8')) == True:
                    continue

                self.rtos.sendMsg (msg)
            except OSError:
                LOGE ("appProcess disconnected")
                self.bleComm.clientSock.close ()
                self.bleComm.sock      .close ()
                break

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
                break
    
    def accelerometerProcess (self):
        while self.accelerometer.isExiting () == False:
            try:
                self.accelerometer.process ()
                time.sleep (3)
            except OSError:
                LOGE ("accelerometerProcess disconnected")
                break
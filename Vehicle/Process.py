import time
import Paths

from   App                    import App
from   Rtos                   import Rtos
from   Mpu9250                import Mpu9250
from   BleComm                import BleComm
from   LoggerHw               import *
from   Settings               import Settings
from   BleParserAndSerializer import BleParserAndSerializer

class Process:
    module                 = __name__
    rtos                   = Rtos                   ()
    settings               = Settings               ()
    app                    = App                    (settings)
    bleParserAndSerializer = BleParserAndSerializer (settings)
    
    def __init__ (self):
        loggerHw = LoggerHw ()
        Logger.setInst (loggerHw)
        
        self.bleComm = BleComm (self.settings)
        self.imu     = Mpu9250 (self.settings)

        self.appThread = self.rtos.createThread (self.appProcess)
        self.appThread.start ()

        self.imuThread = self.rtos.createThread (self.imuProcess)
        self.imuThread.start ()
        
        self.bleServerThread = self.rtos.createThread (self.bleServerProcess)
        self.bleServerThread.start ()
    
        self.appThread      .join  ()
        self.imuThread      .join  ()
        self.bleServerThread.join  ()

    def isBleProcessRunning (self):
        return True
    
    def bleServerProcess (self):
        LOGI (self.module, "bleServerProcess")
        
        while self.isBleProcessRunning ():
            try:
                msg = self.bleComm.clientSock.recv (1024)
                if self.app.isMsgDoubled (msg.decode ('UTF-8')) == True:
                    continue

                self.rtos.sendMsg (msg)
            except OSError:
                LOGE (self.module, "bleServerProcess disconnected")
                #self.bleComm.clientSock.close ()
                #self.bleComm.sock      .close ()
                break

    def appProcess (self):
        LOGI (self.module, "appProcess")
        
        while self.app.isExiting () == False:
            try:
                if self.app.isRunning () == True:
                    msg = self.rtos.getMsg            ()
                    LOGI                              (self.module, f"Received: {msg}")
                    self.bleParserAndSerializer.parse (msg)
                    self.app.process                  ()
                elif self.app.isPaused () == True:
                    self.settings.freeSpin = True

            except OSError:
                LOGE (self.module, "appProcess disconnected")
                break
    
    def imuProcess (self):
        LOGI (self.module, "imuProcess")
        
        while self.imu.isExiting () == False:
            try:
                self.imu.process ()
                time.sleep (5)
            except OSError:
                LOGE (self.module, "imuProcess disconnected")
                break
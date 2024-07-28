import time
import Paths

from   App           import App
from   Rtos          import Rtos
from   Mpu9250       import Mpu9250
from   BleComm       import BleComm
from   LoggerHw      import *
from   Settings      import Settings
from   CmdParser     import CmdParser
from   CmdSerializer import CmdSerializer

class Process:
    module = __name__
    
    def __init__ (self):
        loggerHw = LoggerHw ()
        Logger.setInst (loggerHw)

        self.rtos          = Rtos          ()
        self.settings      = Settings      ()
        self.app           = App           (self.settings)
        self.cmdParser     = CmdParser     (self.settings)
        self.cmdSerializer = CmdSerializer (self.settings)
        self.bleComm       = BleComm       (self.rtos, self.settings)
        self.imu           = Mpu9250       (self.settings)

        self.appThread = self.rtos.createThread (self.appProcess)
        self.appThread.start ()

        self.imuThread = self.rtos.createThread (self.imuProcess)
        self.imuThread.start ()

        self.bleSendThread = self.rtos.createThread (self.bleSendProcess)
        self.bleSendThread.start ()
        
        self.bleReceiveThread = self.rtos.createThread (self.bleReceiveProcess)
        self.bleReceiveThread.start ()
    
        self.appThread       .join  ()
        self.imuThread       .join  ()
        self.bleSendThread   .join  ()
        self.bleReceiveThread.join  ()

    def appProcess (self):
        LOGI (self.module, "appProcess")
        
        try:
            while self.app.isRunning ():
                msg = self.rtos.getCmdQueue ()
                LOGI (self.module, f"Received: {msg}")
                self.cmdParser.parse (msg)
                self.app.process ()
        except OSError:
            pass
    
    def imuProcess (self):
        LOGI (self.module, "imuProcess")
        
        try:
            while self.imu.isRunning ():
                self.imu.process ()
                msg = self.cmdSerializer.imu ()
                self.rtos.addImuQueue (msg)
                time.sleep (5)
        except OSError:
            pass

    def bleSendProcess (self):
        LOGI (self.module, "bleSendProcess")

        try:
            while self.bleComm.isSendRunning ():
                msg = self.rtos.getImuQueue ()
                if not msg:
                    time.sleep (1)
                    break
                self.bleComm.send (msg)
        except OSError:
            pass
    
    def bleReceiveProcess (self):
        LOGI (self.module, "bleReceiveProcess")
        
        try:
            while self.bleComm.isReceiveRunning ():
                msg = self.bleComm.receive ()
                if not msg:
                    time.sleep (1)
                    break
                self.rtos.addCmdQueue (msg)
        except OSError:
            self.bleComm.close ()
            pass
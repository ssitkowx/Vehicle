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
        
        while self.app.isRunning ():
            try:
                    msg = self.rtos.getCmdQueue ()
                    LOGI (self.module, f"Received: {msg}")
                    self.cmdParser.parse (msg)
                    self.app.process ()
            except OSError:
                break
    
    def imuProcess (self):
        LOGI (self.module, "imuProcess")
        
        while self.imu.isRunning ():
            try:
                self.imu.process ()
                msg = self.cmdSerializer.imu ()
                self.rtos.addImuQueue (msg)
                time.sleep (5)
            except OSError:
                break

    def bleSendProcess (self):
        LOGI (self.module, "bleSendProcess")

        while self.bleComm.isSendRunning ():
            try:
                msg = self.rtos.getImuQueue ()
                self.bleComm.send (msg)
            except self.rtos.imuQueue.Empty:
                continue
    
    def bleReceiveProcess (self):
        LOGI (self.module, "bleReceiveProcess")
        
        while self.bleComm.isReceiveRunning ():
            try:
                msg = self.bleComm.receive ()
                if msg == "Unconnected":
                    time.sleep (1)
                    continue
                self.rtos.addCmdQueue (msg)
            except OSError:
                #self.bleComm.clientSock.close ()
                #self.bleComm.sock      .close ()
                break
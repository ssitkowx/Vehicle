import sys
import time
import Paths

from   BleComm           import BleComm
from   LoggerHw          import *
from   Settings          import Settings
from   CmdParser         import CmdParser
from   ControlPanel      import ControlPanel
from   PySide6.QtCore    import QObject, QThread
from   PySide6.QtWidgets import QApplication

class Process:
    def __init__ (self):
        self.settings              = Settings            ()
        self.bleComm               = BleComm             ()
        self.cmdParser             = CmdParser           (self.settings)
        app                        = QApplication        (sys.argv)
        controlPanel               = ControlPanel        (self.settings, self.bleComm)
        self.bleCommSendProcess    = self.bleCommSend    (self.bleComm, self.cmdParser)
        self.bleCommReceiveProcess = self.bleCommReceive (self.bleComm, self.cmdParser)
        controlPanel.show ()
        app         .exec ()

    class bleCommSend (QObject):
        module = __name__

        def __init__ (self, vBleComm: BleComm, vCmdParser: CmdParser):
            super ().__init__ ()
            self.bleComm   = vBleComm
            self.cmdParser = vCmdParser
            self.thread    = QThread ()
            self.task      = self

            self.task.moveToThread        (self.thread)
            self.thread .started .connect (self.task.process)
            self.thread .start            ()
        
        def process (self):
            LOGI (self.module, "bleCommSend")

            while self.bleComm.isRunning ():
                msg = self.rtos.getQueueMsg ()    # rtos not defined
                self.bleComm.send (msg)

    class bleCommReceive (QObject):
        module = __name__

        def __init__ (self, vBleComm: BleComm, vCmdParser: CmdParser):
            super ().__init__ ()
            self.bleComm   = vBleComm
            self.cmdParser = vCmdParser
            self.thread    = QThread      ()
            self.task      = self

            self.task.moveToThread       (self.thread)
            self.thread.started .connect (self.task.process)
            self.thread.start            ()
        
        def process (self):
            LOGI (self.module, "bleCommReceive")

            while self.bleComm.isRunning ():
                try:
                    msg = self.bleComm.receive ()
                    self.cmdParser.parse (msg)

                except OSError:
                    LOGE (self.module, "bleCommReceive disconnected")
                    #self.bleComm.clientSock.close ()
                    #self.bleComm.sock      .close ()
                    break

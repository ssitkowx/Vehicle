import sys
import time
import Paths

from   Rtos              import Rtos
from   BleComm           import BleComm
from   LoggerHw          import *
from   Settings          import Settings
from   CmdParser         import CmdParser
from   ControlPanel      import ControlPanel
from   PySide6.QtCore    import QObject, QThread
from   PySide6.QtWidgets import QApplication

class Process:
    def __init__ (self):
        self.rtos                  = Rtos                ()
        self.settings              = Settings            ()
        self.bleComm               = BleComm             (self.rtos)
        self.cmdParser             = CmdParser           (self.settings)
        app                        = QApplication        (sys.argv)
        controlPanel               = ControlPanel        (self.settings, self.rtos, self.bleComm)
        self.bleCommSendProcess    = self.bleCommSend    (self.rtos, self.bleComm, self.cmdParser)
        self.bleCommReceiveProcess = self.bleCommReceive (self.rtos, self.bleComm, self.cmdParser)
        controlPanel.show ()
        app         .exec ()

    class bleCommSend (QObject):
        module = __name__

        def __init__ (self, vRtos: Rtos, vBleComm: BleComm, vCmdParser: CmdParser):
            super ().__init__ ()
            self.task      = self
            self.rtos      = vRtos
            self.bleComm   = vBleComm
            self.cmdParser = vCmdParser
            self.thread    = QThread     ()
            self.task.moveToThread       (self.thread)
            self.thread .started.connect (self.task.process)
            self.thread .start           ()

        def process (self):
            LOGI (self.module, "bleCommSend")

            while self.bleComm.isRunning ():
                try:
                    msg = self.rtos.getCmdQueue ()
                    self.bleComm.send (msg)
                except OSError:
                    break

    class bleCommReceive (QObject):
        module = __name__

        def __init__ (self, vRtos: Rtos, vBleComm: BleComm, vCmdParser: CmdParser):
            super ().__init__ ()
            self.task      = self
            self.rtos      = vRtos
            self.bleComm   = vBleComm
            self.cmdParser = vCmdParser
            self.thread    = QThread    ()
            self.task.moveToThread      (self.thread)
            self.thread.started.connect (self.task.process)
            self.thread.start           ()

        def process (self):
            LOGI (self.module, "bleCommReceive")

            try:
                while self.bleComm.isRunning ():
                    msg = self.bleComm.receive ()
                    if msg == "Unconnected":
                        time.sleep (1)
                        continue
                    self.cmdParser.parse (msg)
            except OSError:
                self.bleComm.close ()
                pass

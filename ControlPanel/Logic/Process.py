import sys
import Paths

from   Settings          import Settings
from   ControlPanel      import ControlPanel
from   PySide6.QtCore    import QThread
from   PySide6.QtWidgets import QApplication

class Process:
    def __init__ (self):
        self.settings = Settings     ()
        app           = QApplication (sys.argv)
        controlPanel  = ControlPanel (self.settings)
        controlPanel.show            ()
        app         .exec            ()

        #self.bleServerThread = QThread()
        #self.bleServerProcess = self.bleServerProcess ()

        #self.bleServerProcess.moveToThread(self.bleServerThread)

        #self.thread.started.connect(self.worker.run)
        #self.worker.finished.connect(self.thread.quit)
        #self.worker.finished.connect(self.worker.deleteLater)
        #self.thread.finished.connect(self.thread.deleteLater)
        #self.worker.progress.connect(self.reportProgress)

    def startThread(self):
        self.thread.start()
        self.button.setEnabled(False)
        self.thread.finished.connect(lambda: self.button.setEnabled(True))

    def bleServerProcess (self):
        LOGI (self.module, "bleServerProcess")
        
        while self.bleComm.isRunning ():
            try:
                msg = self.bleComm.clientSock.recv (1024)
                #self.rtos.addQueueMsg (msg)
            except OSError:
                LOGE (self.module, "bleServerProcess disconnected")
                #self.bleComm.clientSock.close ()
                #self.bleComm.sock      .close ()
                break
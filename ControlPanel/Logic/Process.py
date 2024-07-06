import sys
import Paths

from Rtos              import Rtos
from Settings          import Settings
from LoggerHw          import LoggerHw
from ControlPanel      import ControlPanel
from PySide6.QtWidgets import QApplication, QWidget

class Process:
    def __init__ (self):
        self.rtos     = Rtos         ()
        self.settings = Settings     ()
        app           = QApplication (sys.argv)
        controlPanel  = ControlPanel (self.settings)
        controlPanel.show            ()
        app         .exec            ()

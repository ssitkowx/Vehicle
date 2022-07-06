from Paths             import *
from Rtos              import Rtos
from Settings          import Settings
from ControlPanel      import ControlPanel
from PySide6.QtWidgets import QApplication

class Task:
    def __init__ (self):
        self.rtos     = Rtos         ()
        self.settings = Settings     ()
        app           = QApplication (sys.argv)
        controlPanel  = ControlPanel (self.settings)
        controlPanel.show            ()
        app         .exec            ()

import sys
import Paths

from   Settings          import Settings
from   ControlPanel      import ControlPanel
from   PySide6.QtWidgets import QApplication

class Process:
    def __init__ (self):
        self.settings = Settings     ()
        app           = QApplication (sys.argv)
        controlPanel  = ControlPanel (self.settings)
        controlPanel.show            ()
        app         .exec            ()

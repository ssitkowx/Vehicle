from PySide6.QtCore import QTimer
from Settings       import Settings

class Timer:
    def __init__ (self):
        self.obj = QTimer ()
        self.obj.start (Settings.Duty.TIMEOUT)

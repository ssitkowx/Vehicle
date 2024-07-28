from PySide6.QtCore import QTimer
from Settings       import Settings

class Timer:
    TimeoutInMs = 200

    def __init__ (self):
        self.obj = QTimer ()
        self.obj.start (Timer.TimeoutInMs)

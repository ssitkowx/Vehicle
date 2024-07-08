from PySide6.QtCore import QTimer

class Timer:
    def __init__ (self):
        self.obj = QTimer ()
        self.obj.start (100)

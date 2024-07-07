from PySide6.QtWidgets import QLabel

class Labels:
    def __init__ (self):
        self.roll  = QLabel ("Roll: ")
        self.pitch = QLabel ("Pitch: ")
        self.yaw   = QLabel ("Yaw: ")

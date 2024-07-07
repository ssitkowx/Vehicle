from PySide6.QtWidgets import QLabel

class Labels:
    def __init__ (self):
        self.rollLabel  = QLabel ("Roll: ")
        self.pitchLabel = QLabel ("Pitch: ")
        self.yawLabel   = QLabel ("Yaw: ")

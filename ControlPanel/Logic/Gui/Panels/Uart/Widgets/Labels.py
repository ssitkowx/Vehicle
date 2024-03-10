from PySide6.QtWidgets import QLabel

class Labels:
    def __init__ (self):
        self.portLabel        = QLabel ("Port")
        self.speedLabel       = QLabel ("Speed(baud)")
        self.passwordLabel    = QLabel ("Password")
        self.dataBitsLabel    = QLabel ("Data bits")
        self.stopBitsLabel    = QLabel ("Stop bits")
        self.parityBitsLabel  = QLabel ("Parity bits")
        self.flowControlLabel = QLabel ("Flow control")
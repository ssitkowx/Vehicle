from PySide6.QtWidgets import QLabel

class Labels:
    def __init__ (self):
        self.port        = QLabel ("Port")
        self.speed       = QLabel ("Speed(baud)")
        self.password    = QLabel ("Password")
        self.dataBits    = QLabel ("Data bits")
        self.stopBits    = QLabel ("Stop bits")
        self.parityBits  = QLabel ("Parity bits")
        self.flowControl = QLabel ("Flow control")
from PySide6.QtWidgets import QComboBox

class ComboBoxes:
    ports       = []
    speeds      = ('1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200')
    dataBits    = ('5', '6', '7', '8')
    stopBits    = ('1', '2', '1.5')
    parityBits  = ('No', 'Even', 'Odd', 'Space', 'Mark')
    flowControl = ('No', 'RTS/CTS', 'XON/XOFF')
    
    def __init__ (self):
        self.portComboBox = QComboBox()
        
        self.speedComboBox = QComboBox     ()
        self.speedComboBox.addItems        (self.speeds)
        self.speedComboBox.setCurrentIndex (7)
        
        self.dataBitsComboBox = QComboBox     ()
        self.dataBitsComboBox.addItems        (self.dataBits)
        self.dataBitsComboBox.setCurrentIndex (3)
        
        self.stopBitsComboBox = QComboBox     ()
        self.stopBitsComboBox.addItems        (self.stopBits)
        self.stopBitsComboBox.setCurrentIndex (0)
        
        self.parityBitsComboBox = QComboBox     ()
        self.parityBitsComboBox.addItems        (self.parityBits)
        self.parityBitsComboBox.setCurrentIndex (0)
        
        self.flowControlComboBox = QComboBox     ()
        self.flowControlComboBox.addItems        (self.flowControl)
        self.flowControlComboBox.setCurrentIndex (0)
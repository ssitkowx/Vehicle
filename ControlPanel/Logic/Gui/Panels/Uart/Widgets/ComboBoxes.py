from PySide6.QtWidgets import QComboBox

class ComboBoxes:
    ports       = []
    speeds      = ('1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200')
    dataBits    = ('5', '6', '7', '8')
    stopBits    = ('1', '2', '1.5')
    parityBits  = ('No', 'Even', 'Odd', 'Space', 'Mark')
    flowControl = ('No', 'RTS/CTS', 'XON/XOFF')
    
    def __init__ (self):
        self.port = QComboBox()
        
        self.speed = QComboBox     ()
        self.speed.addItems        (ComboBoxes.speeds)
        self.speed.setCurrentIndex (7)
        
        self.dataBits = QComboBox     ()
        self.dataBits.addItems        (ComboBoxes.dataBits)
        self.dataBits.setCurrentIndex (3)
        
        self.stopBits = QComboBox     ()
        self.stopBits.addItems        (ComboBoxes.stopBits)
        self.stopBits.setCurrentIndex (0)
        
        self.parityBits = QComboBox     ()
        self.parityBits.addItems        (ComboBoxes.parityBits)
        self.parityBits.setCurrentIndex (0)
        
        self.flowControl = QComboBox     ()
        self.flowControl.addItems        (ComboBoxes.flowControl)
        self.flowControl.setCurrentIndex (0)
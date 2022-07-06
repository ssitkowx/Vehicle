from PySide6.QtWidgets import QComboBox

class ComboBoxes():
    Ports       = []
    Speeds      = ('1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200')
    DataBits    = ('5', '6', '7', '8')
    StopBits    = ('1', '2', '1.5')
    ParityBits  = ('No', 'Even', 'Odd', 'Space', 'Mark')
    FlowControl = ('No', 'RTS/CTS', 'XON/XOFF')
    
    def __init__(self):
        self.portComboBox = QComboBox()
        
        self.speedComboBox = QComboBox          ()
        self.speedComboBox.addItems             (self.Speeds)
        self.speedComboBox.setCurrentIndex      (7)
        
        self.dataBitsComboBox = QComboBox       ()
        self.dataBitsComboBox.addItems          (self.DataBits)
        self.dataBitsComboBox.setCurrentIndex   (3)
        
        self.stopBitsComboBox = QComboBox       ()
        self.stopBitsComboBox.addItems          (self.StopBits)
        self.stopBitsComboBox.setCurrentIndex   (0)
        
        self.parityBitsComboBox = QComboBox     ()
        self.parityBitsComboBox.addItems        (self.ParityBits)
        self.parityBitsComboBox.setCurrentIndex (0)
        
        self.flowControlComboBox = QComboBox    ()
        self.flowControlComboBox.addItems       (self.FlowControl)
        self.flowControlComboBox.setCurrentIndex(0)
from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

class Layout:
    def __init__ (self, vLabel, vComboBox, vButton, vLineEdit):
        port = QHBoxLayout ()
        port.addWidget (vLabel.port)
        port.addWidget (vComboBox.port)
        
        speed = QHBoxLayout ()
        speed.addWidget (vLabel.speed)
        speed.addWidget (vComboBox.speed)
        
        dataBits = QHBoxLayout ()
        dataBits.addWidget (vLabel.dataBits)
        dataBits.addWidget (vComboBox.dataBits)
        
        stopBits = QHBoxLayout ()
        stopBits.addWidget (vLabel.stopBits)
        stopBits.addWidget (vComboBox.stopBits)
        
        parityBits = QHBoxLayout ()
        parityBits.addWidget (vLabel.parityBits)
        parityBits.addWidget (vComboBox.parityBits)
        
        flowControl = QHBoxLayout ()
        flowControl.addWidget (vLabel.flowControl)
        flowControl.addWidget (vComboBox.flowControl)
        
        saveButton = QVBoxLayout ()
        saveButton.setAlignment (Qt.AlignCenter)
        saveButton.addWidget    (vButton.save)
        
        password = QHBoxLayout ()
        password.addWidget (vLabel.password)
        password.addWidget (vLineEdit.password)
        
        self.obj = QVBoxLayout ()
        self.obj.addLayout (port)
        self.obj.addLayout (speed)
        self.obj.addLayout (dataBits)
        self.obj.addLayout (stopBits)
        self.obj.addLayout (parityBits)
        self.obj.addLayout (flowControl)
        self.obj.addLayout (password)
        self.obj.addLayout (saveButton)
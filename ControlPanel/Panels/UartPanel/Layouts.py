from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

class Layouts():
    def __init__(self):
        layoutPort = QHBoxLayout       ()
        layoutPort.addWidget           (self.portLabel)
        layoutPort.addWidget           (self.portComboBox)
        
        layoutSpeed = QHBoxLayout      ()
        layoutSpeed.addWidget          (self.speedLabel)
        layoutSpeed.addWidget          (self.speedComboBox)
        
        layoutDataBits = QHBoxLayout   ()
        layoutDataBits.addWidget       (self.dataBitsLabel)
        layoutDataBits.addWidget       (self.dataBitsComboBox)
        
        layoutStopBits = QHBoxLayout   ()
        layoutStopBits.addWidget       (self.stopBitsLabel)
        layoutStopBits.addWidget       (self.stopBitsComboBox)
        
        layoutParityBits = QHBoxLayout ()
        layoutParityBits.addWidget     (self.parityBitsLabel)
        layoutParityBits.addWidget     (self.parityBitsComboBox)
        
        layoutFlowControl = QHBoxLayout()
        layoutFlowControl.addWidget    (self.flowControlLabel)
        layoutFlowControl.addWidget    (self.flowControlComboBox)
        
        layoutSaveButton = QVBoxLayout ()
        layoutSaveButton.setAlignment  (Qt.AlignCenter)
        layoutSaveButton.addWidget     (self.saveButton)
        
        layoutPassword = QHBoxLayout   ()
        layoutPassword.addWidget       (self.passwordLabel)
        layoutPassword.addWidget       (self.passwordLineEdit)
        
        layout = QVBoxLayout           ()
        layout.addLayout               (layoutPort)
        layout.addLayout               (layoutSpeed)
        layout.addLayout               (layoutDataBits)
        layout.addLayout               (layoutStopBits)
        layout.addLayout               (layoutParityBits)
        layout.addLayout               (layoutFlowControl)
        layout.addLayout               (layoutPassword)
        layout.addLayout               (layoutSaveButton)
        
        self.widget = QWidget          (self)
        self.widget.setLayout          (layout)
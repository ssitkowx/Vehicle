from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

class Layouts:
    def __init__ (self):
        layoutUuid = QHBoxLayout       ()
        layoutUuid.addWidget           (self.uuidLabel)
        layoutUuid.addWidget           (self.uuidComboBox)
        
        layoutAddress = QHBoxLayout    ()
        layoutAddress.addWidget        (self.addressLabel)
        layoutAddress.addWidget        (self.addressComboBox)
        
        layoutSaveButton = QVBoxLayout ()
        layoutSaveButton.setAlignment  (Qt.AlignCenter)
        layoutSaveButton.addWidget     (self.saveButton)
        
        layout = QVBoxLayout           ()
        layout.addLayout               (layoutUuid)
        layout.addLayout               (layoutAddress)
        layout.addLayout               (layoutSaveButton)
        
        self.widget = QWidget          (self)
        self.widget.setLayout          (layout)
from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

class Layout:
    def __init__ (self, vLabels, vComboBoxex, vButton):
        uuid = QHBoxLayout ()
        uuid.addWidget     (vLabels.uuid)
        uuid.addWidget     (vComboBoxex.uuid)
        
        address = QHBoxLayout ()
        address.addWidget     (vLabels.address)
        address.addWidget     (vComboBoxex.address)
        
        saveButton = QVBoxLayout ()
        saveButton.setAlignment  (Qt.AlignCenter)
        saveButton.addWidget     (vButton.save)
        
        self.obj = QVBoxLayout ()
        self.obj.addLayout     (uuid)
        self.obj.addLayout     (address)
        self.obj.addLayout     (saveButton)
from PySide6.QtWidgets import QComboBox

class ComboBox:
    uuids     = []
    addresses = []
    
    def __init__ (self):
        self.uuidComboBox = QComboBox     ()
        self.uuidComboBox.addItems        (self.uuids)
        self.uuidComboBox.setEditable     (True)
        self.uuidComboBox.setCurrentIndex (5)
        
        self.addressComboBox = QComboBox     ()
        self.addressComboBox.addItems        (self.addresses)
        self.addressComboBox.setEditable     (True)
        self.addressComboBox.setCurrentIndex (5)
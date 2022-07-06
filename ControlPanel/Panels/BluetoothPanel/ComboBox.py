from PySide6.QtWidgets import QComboBox

class ComboBox:
    Uuids     = []
    Addresses = []
    
    def __init__(self):
        self.uuidComboBox = QComboBox        ()
        self.uuidComboBox.addItems           (self.Uuids)
        self.uuidComboBox.setEditable        (True)
        self.uuidComboBox.setCurrentIndex    (5)
        
        self.addressComboBox = QComboBox     ()
        self.addressComboBox.addItems        (self.Addresses)
        self.addressComboBox.setEditable     (True)
        self.addressComboBox.setCurrentIndex (5)
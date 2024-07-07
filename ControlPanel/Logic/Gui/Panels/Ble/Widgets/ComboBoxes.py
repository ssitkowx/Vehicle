from PySide6.QtWidgets import QComboBox

class ComboBoxes:
    uuids     = []
    addresses = []
    
    def __init__ (self):
        self.uuid = QComboBox     ()
        self.uuid.addItems        (self.uuids)
        self.uuid.setEditable     (True)
        self.uuid.setCurrentIndex (5)
        
        self.address = QComboBox     ()
        self.address.addItems        (self.addresses)
        self.address.setEditable     (True)
        self.address.setCurrentIndex (5)
from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QCheckBox

class CheckBox:
    def __init__(self):
        self.interfaceCheckBox = QCheckBox          ("To uart", self)
        self.interfaceCheckBox.setCheckState        (Qt.Unchecked)
        self.interfaceCheckBox.stateChanged.connect (self.ChooseInterface)

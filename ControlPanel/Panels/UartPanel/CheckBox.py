from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QCheckBox

class CheckBox():
    def __init__(self):
        self.passwordCheckBox = QCheckBox         ("Password", self)
        self.passwordCheckBox.setCheckState       (Qt.Unchecked)
        self.passwordCheckBox.stateChanged.connect(self.HidePassword)

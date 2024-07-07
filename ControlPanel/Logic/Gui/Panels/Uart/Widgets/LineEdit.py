from PySide6.QtWidgets import QLineEdit

class LineEdit:
    def __init__ (self):
        self.password = QLineEdit        ()
        self.password.setEchoMode        (QLineEdit.EchoMode.Normal)
        self.password.setPlaceholderText ('Enter password')
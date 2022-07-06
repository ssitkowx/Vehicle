from PySide6.QtWidgets import QLineEdit

class LineEdit():
    def __init__(self):
        self.passwordLineEdit = QLineEdit       ()
        self.passwordLineEdit.setEchoMode       (QLineEdit.EchoMode.Normal)
        self.passwordLineEdit.setPlaceholderText('Enter password')
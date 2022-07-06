from PySide6.QtWidgets import QLineEdit

class LineEdit:
    def __init__(self):
        self.commandLineEdit = QLineEdit       ()
        self.commandLineEdit.setMaxLength      (30)
        self.commandLineEdit.setPlaceholderText("Enter command")
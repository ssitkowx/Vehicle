from PySide6.QtCore    import QSize
from PySide6.QtWidgets import QPushButton

class Button:
    def __init__ (self):
        dimensions      = QSize         (200, 50)
        self.saveButton = QPushButton   ("Save")
        self.saveButton.setFixedSize    (dimensions.width(), dimensions.height())
        self.saveButton.clicked.connect (self.SaveClicked)
        self.saveButton.setStyleSheet   ('background-color:blue')

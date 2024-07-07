from PySide6.QtCore    import QSize
from PySide6.QtWidgets import QPushButton

class Button:
    def __init__ (self):
        dimensions      = QSize         (200, 50)
        self.saveButton = QPushButton   ("Connect")
        self.saveButton.setFixedSize    (dimensions.width(), dimensions.height())
        self.saveButton.clicked.connect (self.connectClicked)
        self.saveButton.setStyleSheet   ('background-color:blue')

from PySide6.QtCore    import QSize
from PySide6.QtWidgets import QPushButton

class Button:
    def __init__ (self):
        dimensions = QSize      (200, 50)
        self.save = QPushButton ("Connect")
        self.save.setFixedSize  (dimensions.width(), dimensions.height())
        self.save.setStyleSheet ('background-color:blue')

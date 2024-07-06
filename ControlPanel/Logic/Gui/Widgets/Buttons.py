from PySide6.QtCore import QSize
from PySide6.QtWidgets import QPushButton, QSizePolicy

class Buttons:
    def __init__(self):
        size = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        width  = 200
        height = 60
        self.leftButton = QPushButton    ("Left")
        self.leftButton.setMinimumHeight (height)
        self.leftButton.setStyleSheet    ('color: black; background-color:brown')
        self.leftButton.setSizePolicy    (size)

        self.rightButton = QPushButton    ("Right")
        self.rightButton.setMinimumHeight (height)
        self.rightButton.setStyleSheet    ('color: black; background-color:brown')
        self.rightButton.setSizePolicy    (size)

        self.forwardButton = QPushButton  ("Forward")
        self.forwardButton.setMinimumSize (QSize(width, height))
        self.forwardButton.setStyleSheet  ('color: black; background-color:brown')
        self.forwardButton.setSizePolicy  (size)

        self.backwardButton = QPushButton  ("Backward")
        self.backwardButton.setMinimumSize (QSize(width, height))
        self.backwardButton.setStyleSheet  ('color: black; background-color:brown')
        self.backwardButton.setSizePolicy  (size)
        
        self.clearLogsButton = QPushButton   ("Clear logs")
        self.clearLogsButton.clicked.connect (self.clearButtonClicked)
        self.clearLogsButton.setStyleSheet   ('background-color:blue')
        self.clearLogsButton.setMaximumWidth (75)
        self.clearLogsButton.setSizePolicy   (size)

    def changeColor(self, vButton, vIsPressed):
        if vIsPressed: vButton.setStyleSheet('color: white; background-color:black')
        else:          vButton.setStyleSheet('color: black; background-color:brown')
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QPushButton, QSizePolicy

class Buttons:
    def __init__(self):
        size = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        width  = 200
        height = 60
        self.left = QPushButton    ("Left")
        self.left.setMinimumHeight (height)
        self.left.setStyleSheet    ('color: black; background-color:brown')
        self.left.setSizePolicy    (size)

        self.right = QPushButton    ("Right")
        self.right.setMinimumHeight (height)
        self.right.setStyleSheet    ('color: black; background-color:brown')
        self.right.setSizePolicy    (size)

        self.forward = QPushButton  ("Forward")
        self.forward.setMinimumSize (QSize(width, height))
        self.forward.setStyleSheet  ('color: black; background-color:brown')
        self.forward.setSizePolicy  (size)

        self.backward = QPushButton  ("Backward")
        self.backward.setMinimumSize (QSize(width, height))
        self.backward.setStyleSheet  ('color: black; background-color:brown')
        self.backward.setSizePolicy  (size)
        
        self.clearLogs = QPushButton   ("Clear logs")
        self.clearLogs.setStyleSheet   ('background-color:blue')
        self.clearLogs.setMaximumWidth (75)
        self.clearLogs.setSizePolicy   (size)

    def changeColor(self, vButton, vIsPressed):
        if vIsPressed: vButton.setStyleSheet('color: white; background-color:black')
        else:          vButton.setStyleSheet('color: black; background-color:brown')
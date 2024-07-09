from PySide6.QtCore import QSize
from PySide6.QtWidgets import QPushButton, QSizePolicy

class Buttons:
    left     = 's'
    right    = 'f'
    forward  = 'e'
    backward = 'd'

    def __init__(self):
        size = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        width  = 200
        height = 60
        self.left = QPushButton    ("Left")
        self.left.setMinimumHeight (height)
        self.left.setStyleSheet    ('font-weight: bold; color: black; background-color:blue')
        self.left.setSizePolicy    (size)

        self.right = QPushButton    ("Right")
        self.right.setMinimumHeight (height)
        self.right.setStyleSheet    ('font-weight: bold; color: black; background-color:blue')
        self.right.setSizePolicy    (size)

        self.forward = QPushButton  ("Forward")
        self.forward.setMinimumSize (QSize(width, height))
        self.forward.setStyleSheet  ('font-weight: bold; color: black; background-color:blue')
        self.forward.setSizePolicy  (size)

        self.backward = QPushButton  ("Backward")
        self.backward.setMinimumSize (QSize(width, height))
        self.backward.setStyleSheet  ('font-weight: bold; color: black; background-color:blue')
        self.backward.setSizePolicy  (size)
        
        self.clearLogs = QPushButton   ("Clear logs")
        self.clearLogs.setStyleSheet   ('font-weight: bold; background-color:blue')
        self.clearLogs.setMaximumWidth (80)
        self.clearLogs.setSizePolicy   (size)

    def changeColor(self, vButton, vIsPressed):
        if vIsPressed: vButton.setStyleSheet('font-weight: bold; color: white; background-color:darkgreen')
        else:          vButton.setStyleSheet('font-weight: bold; color: black; background-color:blue')
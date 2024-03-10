from PySide6.QtWidgets import QPushButton

class Buttons:
    def __init__(self):
        height             = 50
        self.sendButton    = QPushButton ("Send")
        self.sendButton.setFixedHeight   (height)
        self.sendButton.clicked.connect  (self.sendButtonClicked)
        self.sendButton.setStyleSheet    ('background-color:blue')
        
        self.connectButton = QPushButton   ("Connect")
        self.connectButton.setFixedHeight  (height)
        self.connectButton.clicked.connect (self.connectButtonClicked)
        self.connectButton.setStyleSheet   ('background-color:blue')
        
        self.clearLogsButton = QPushButton   ("Clear logs")
        self.clearLogsButton.setFixedHeight  (height)
        self.clearLogsButton.clicked.connect (self.clearButtonClicked)
        self.clearLogsButton.setStyleSheet   ('background-color:blue')


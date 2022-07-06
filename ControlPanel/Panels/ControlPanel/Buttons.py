from PySide6.QtWidgets import QPushButton

class Buttons:
    def __init__(self):
        height             = 50
        self.sendButton    = QPushButton    ("Send", self)
        self.sendButton.setFixedHeight      (height)
        self.sendButton.clicked.connect     (self.SendButtonClicked)
        self.sendButton.setStyleSheet       ('background-color:blue')
        
        self.connectButton = QPushButton    ("Connect", self)
        self.connectButton.setFixedHeight   (height)
        self.connectButton.clicked.connect  (self.ConnectButtonClicked)
        self.connectButton.setStyleSheet    ('background-color:blue')
        
        self.clearLogsButton = QPushButton  ("Clear logs", self)
        self.clearLogsButton.setFixedHeight (height)
        self.clearLogsButton.clicked.connect(self.ClearButtonClicked)
        self.clearLogsButton.setStyleSheet  ('background-color:blue')


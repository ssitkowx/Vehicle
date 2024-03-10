from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

class Layouts:
    def __init__ (self):
        msgLayout = QHBoxLayout ()
        msgLayout.addWidget (self.commandLineEdit)
        msgLayout.addWidget (self.commandComboBox)
        
        buttonLayout = QHBoxLayout ()
        buttonLayout.addWidget (self.connectButton)
        buttonLayout.addWidget (self.sendButton)
        buttonLayout.addWidget (self.clearLogsButton)
        
        layout = QVBoxLayout ()
        layout.addLayout  (msgLayout)
        layout.addLayout  (buttonLayout)
        layout.addWidget  (self.interfaceCheckBox)
        layout.addWidget  (self.textBrowser)
        layout.setSpacing (20)
        
        self.widgetLayout = QWidget ()
        self.widgetLayout.setLayout (layout)

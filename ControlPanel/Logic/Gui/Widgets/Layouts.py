from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout

class Layouts:
    def __init__ (self):
        self.widgetLayout = QWidget ()
        layout = QVBoxLayout ()
        
        controlPanelGroupBox   = QGroupBox ("Control panel")
        controlPanelGroupBox.setStyleSheet("QGroupBox { background-color: white; }")
        
        controlPanelGridLayout = QGridLayout ()
        controlPanelGridLayout.addWidget (self.forwardButton , 0, 1)
        controlPanelGridLayout.addWidget (self.leftButton    , 1, 0)
        controlPanelGridLayout.addWidget (self.rightButton   , 1, 2)
        controlPanelGridLayout.addWidget (self.backwardButton, 2, 1)
        controlPanelGroupBox  .setLayout (controlPanelGridLayout)

        terminalGroupBox = QGroupBox ("Terminal")
        terminalGroupBox.setStyleSheet("QGroupBox { background-color: gray; }")
        
        terminalLayout   = QHBoxLayout ()
        terminalLayout  .addWidget (self.clearLogsButton)
        terminalLayout  .addWidget (self.textBrowser)
        terminalGroupBox.setLayout (terminalLayout)

        layout.addWidget  (controlPanelGroupBox)
        layout.setSpacing (10)
        layout.addWidget  (terminalGroupBox)
        self.widgetLayout.setLayout (layout)

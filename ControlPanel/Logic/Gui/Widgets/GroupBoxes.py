from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout

class GroupBoxes:
    def __init__ (self, vLabels, vButtons, vTextBrowser):
        params = QGroupBox ("Params")
        params.setStyleSheet("QGroupBox { font-weight: bold; background-color: gray; }")

        paramsLayout = QHBoxLayout ()
        paramsLayout.addWidget (vLabels.duty)
        paramsLayout.addWidget (vLabels.roll)
        paramsLayout.addWidget (vLabels.pitch)
        paramsLayout.addWidget (vLabels.yaw)
        params      .setLayout (paramsLayout)
        
        controlPanel = QGroupBox   ("Control panel")
        controlPanel.setStyleSheet ("QGroupBox { font-weight: bold; background-color: gray; }")
        
        controlPanelGridLayout = QGridLayout ()
        controlPanelGridLayout.addWidget (vButtons.forward , 0, 1)
        controlPanelGridLayout.addWidget (vButtons.left    , 1, 0)
        controlPanelGridLayout.addWidget (vButtons.right   , 1, 2)
        controlPanelGridLayout.addWidget (vButtons.backward, 2, 1)
        controlPanel          .setLayout (controlPanelGridLayout)

        terminalGroupBox = QGroupBox   ("Terminal")
        terminalGroupBox.setStyleSheet ("QGroupBox { font-weight: bold; background-color: gray; }")
        
        terminalLayout = QHBoxLayout ()
        terminalLayout  .addWidget (vButtons.clearLogs)
        terminalLayout  .addWidget (vTextBrowser)
        terminalGroupBox.setLayout (terminalLayout)

        self.obj = QVBoxLayout ()
        self.obj.addWidget  (params)
        self.obj.setSpacing (10)
        self.obj.addWidget  (controlPanel)
        self.obj.setSpacing (10)
        self.obj.addWidget  (terminalGroupBox)

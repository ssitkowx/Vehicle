from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QTextBrowser, QScrollBar

class TextBrowser:
    def __init__(self):
        self.logOutputTextBrowser = QTextBrowser       (self)
        self.logOutputTextBrowser.setVerticalScrollBar (QScrollBar())
        self.logOutputTextBrowser.setStyleSheet        ("background-color:#33ccff")

    def ToogleName(self, v_state):
        if(Qt.Checked == v_state):
            self.checkBox.setText("Uart")
        else:
            self.checkBox.setText("Bluetooth")
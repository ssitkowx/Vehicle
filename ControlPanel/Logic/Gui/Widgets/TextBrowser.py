from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QTextBrowser, QScrollBar

class TextBrowser:
    def __init__ (self):
        self.textBrowser = QTextBrowser       ()
        self.textBrowser.setStyleSheet        ("background-color:white")
        self.textBrowser.setVerticalScrollBar (QScrollBar())

    def toogleName (self, v_state):
        if (Qt.Checked == v_state): self.checkBox.setText ("Uart")
        else:                       self.checkBox.setText ("Bluetooth")
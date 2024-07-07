from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QTextBrowser, QScrollBar

class TextBrowser:
    def __init__ (self):
        self.obj = QTextBrowser       ()
        self.obj.setStyleSheet        ("background-color:white")
        self.obj.setVerticalScrollBar (QScrollBar())

    def toogleName (self, v_state):
        if (Qt.Checked == v_state): self.checkBox.setText ("Uart")
        else:                       self.checkBox.setText ("Bluetooth")
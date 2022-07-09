from PySide6.QtWidgets import QComboBox

class ComboBox:
    Commands = ("Turn left", "Turn right", "Move forward", "Move backward")
    
    def __init__ (self):
        self.commandComboBox = QComboBox                 ()
        self.commandComboBox.currentIndexChanged.connect (self.CurrentIndexChanged)
        self.commandComboBox.addItems                    (self.Commands)
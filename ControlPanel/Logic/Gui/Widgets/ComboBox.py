from PySide6.QtWidgets import QComboBox

class ComboBox:
    commands = ("Turn left", "Turn right", "Move forward", "Move backward")
    
    def __init__ (self):
        self.commandComboBox = QComboBox                 ()
        self.commandComboBox.currentIndexChanged.connect (self.currentIndexChanged)
        self.commandComboBox.addItems                    (self.commands)
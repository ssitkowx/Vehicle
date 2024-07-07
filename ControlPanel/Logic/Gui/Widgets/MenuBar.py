from PySide6.QtGui     import QAction
from PySide6.QtWidgets import QMenuBar

class MenuBar:
    def __init__(self):
        self.uartAction = QAction    ("Uart")
        self.uartAction.setStatusTip ("Configure Uart")
        
        self.bluetoothAction = QAction    ("Bluetooth")
        self.bluetoothAction.setStatusTip ("Configure bluetooth")
        
        self.obj        = QMenuBar         ()
        self.menuConfig = self.obj.addMenu ("Configuration")
        
        self.menuInterface = self.menuConfig.addMenu ("Interface")
        self.menuInterface.addAction (self.uartAction)
        self.menuInterface.addAction (self.bluetoothAction)

from PySide6.QtGui     import QAction
from PySide6.QtWidgets import QMenuBar

class MenuBar:
    def __init__(self):
        uartAction = QAction         ("Uart", self)
        uartAction.setStatusTip      ("Configure Uart")
        uartAction.triggered.connect (self.OpenUartInterface)
        
        bluetoothAction = QAction         ("Bluetooth", self)
        bluetoothAction.setStatusTip      ("Configure bluetooth")
        bluetoothAction.triggered.connect (self.OpenBluetoothInterface)
        
        menuBar    = QMenuBar        ()
        menuConfig = menuBar.addMenu ("Configuration")
        
        menuInterface = menuConfig.addMenu ("Interface")
        menuInterface.addAction (uartAction)
        menuInterface.addAction (bluetoothAction)
        self.setMenuBar         (menuBar)

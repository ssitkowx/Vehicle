from Uart                            import Uart
from Labels                          import Labels
from MenuBar                         import MenuBar
from Buttons                         import Buttons
from BleComm                         import BleComm
from Settings                        import Settings
from GroupBoxes                      import GroupBoxes
from LoggerHw                        import *
from TextBrowser                     import TextBrowser
from PySide6.QtCore                  import QSize, Qt
from CommandConverter                import CommandConverter
from PySide6.QtWidgets               import QMainWindow, QWidget, QLabel
from BleParserAndSerializer          import BleParserAndSerializer
from Logic.Gui.Panels.Ble.BlePanel   import BlePanel
from Logic.Gui.Panels.Uart.UartPanel import UartPanel

from PySide6.QtGui import QKeyEvent

class ControlPanel (QMainWindow, Buttons, MenuBar, TextBrowser, GroupBoxes):
    module = __name__
    
    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__ (self)
        Labels     .__init__ (self)
        Buttons    .__init__ (self)
        MenuBar    .__init__ (self)
        TextBrowser.__init__ (self)
        GroupBoxes    .__init__ (self)
        
        loggerHw = LoggerHw (self.textBrowser)
        Logger.setInst (loggerHw)

        self.uart                   = Uart                   ()
        self.bleComm                = BleComm                ()
        self.blePanel               = BlePanel               (self.bleComm, vSettings)
        self.uartPanel              = UartPanel              (self.uart)
        self.commandConverter       = CommandConverter       (vSettings)
        self.bleParserAndSerializer = BleParserAndSerializer (vSettings)
        self.panel                  = self.uartPanel

        self.setGeometry      (500, 200, 500, 500)
        self.setWindowTitle   ('Control Panel')
        self.setStyleSheet    ('background-color:white;'
                               'selection-color: black;'
                               'selection-background-color: gray;')
        self.setMinimumSize   (QSize(500, 500))
        self.setMaximumSize   (QSize(800, 800))
        self.setCentralWidget (self.widgetLayout)

        #self.central_widget = QWidget(self)
        #self.setCentralWidget(self.central_widget)

        #self.key_label = QLabel("Last Key Pressed: None", self.central_widget)
        #self.key_label.setGeometry(10, 10, 200, 30)

    #def logData (self):
    #    self.textBrowser.append (str (self.uart.Receive ()))

    def sendButtonClicked (self, vChecked):
        data = self.commandLineEdit.text ()
        self.commandConverter.convert (data)

        json = self.bleParserAndSerializer.serialize ()
        LOGI (self.module, "Send {0}".format (json))
        self.panel.send         (json)

    def connectButtonClicked (self, vChecked):
        if (self.connectButton.text () == "Connect"):
            if self.panel.connect () == False: return
            self.connectButton.setText ("Disconnect")
        else:
            self.panel.disconnect ()
            self.connectButton.setText ("Connect")
            LOGW                       (self.module, "Disconnected")

    def clearButtonClicked (self, vChecked):
        self.textBrowser.clear ()

    def openUartInterface (self, vChecked):
        self.uartPanel.show ()

    def openBluetoothInterface (self, vChecked):
        self.blePanel.show ()

    def chooseInterface (self, vState):
        if vState == 0:
            self.panel = self.uartPanel
            self.interfaceCheckBox.setText ("Terminal")
        else:
            self.panel = self.blePanel
            self.interfaceCheckBox.setText ("Car")

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            key_num = event.key ()
            self.key_label.setText(f"Last Key Pressed: {key_num}")

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            key_num = event.key ()
            self.key_label.setText(f"Key Released: {key_num}")
'''
    def keyPressEvent(self, event):
        self.rollLabel.setText("Pressed")
        if event.key () == Qt.Key_Up:
            self.changeColor (self.forwardButton, True)
        elif event.key () == Qt.Key_Down:
            self.changeColor (self.backwardButton, True)
        elif event.key () == Qt.Key_Left:
            self.changeColor (self.leftButton, True)
        elif event.key () == Qt.Key_Right:
            self.changeColor (self.rightButton, True)
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        self.rollLabel.setText("Released")
        if event.key () == Qt.Key_Up:
            self.changeColor (self.forwardButton, False)
        elif event.key () == Qt.Key_Down:
            self.changeColor (self.backwardButton, False)
        elif event.key () == Qt.Key_Left:
            self.changeColor(self.leftButton, False)
        elif event.key () == Qt.Key_Right:
            self.changeColor(self.rightButton, False)
        else:
            super().keyPressEvent(event)
'''
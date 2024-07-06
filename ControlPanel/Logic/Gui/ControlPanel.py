from Uart                            import Uart
from MenuBar                         import MenuBar
from Buttons                         import Buttons
from Layouts                         import Layouts
from BleComm                         import BleComm
from Settings                        import Settings
from LineEdit                        import LineEdit
from Keyboard                        import Keyboard
from LoggerHw                        import *
from TextBrowser                     import TextBrowser
from PySide6.QtCore                  import QSize, Qt
from CommandConverter                import CommandConverter
from PySide6.QtWidgets               import QMainWindow, QPushButton
from BleParserAndSerializer          import BleParserAndSerializer
from Logic.Gui.Panels.Ble.BlePanel   import BlePanel
from Logic.Gui.Panels.Uart.UartPanel import UartPanel

class ControlPanel (QMainWindow, Buttons, MenuBar, LineEdit, TextBrowser, Layouts):
    module = __name__
    
    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__ (self)
        Buttons    .__init__ (self)
        MenuBar    .__init__ (self)
        LineEdit   .__init__ (self)
        TextBrowser.__init__ (self)
        Layouts    .__init__ (self)
        
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

        #self.keyboard.show()

    #def logData (self):
    #    self.textBrowser.append (str (self.uart.Receive ()))

    def currentIndexChanged (self, vIndex):
        self.commandLineEdit.setText (self.commandComboBox.currentText ())

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
        if event.key () == Qt.Key_Up:
            self.changeColor (self.forwardButton, True)
        elif event.key () == Qt.Key_Down:
            self.changeColor (self.backwardButton, True)
        elif event.key () == Qt.Key_Left:
            self.changeColor (self.leftButton, True)
        elif event.key () == Qt.Key_Right:
            self.changeColor (self.rightButton, True)

    def keyReleaseEvent(self, event):
        if event.key () == Qt.Key_Up:
            self.changeColor (self.forwardButton, False)
        elif event.key () == Qt.Key_Down:
            self.changeColor (self.backwardButton, False)
        elif event.key () == Qt.Key_Left:
            self.changeColor(self.leftButton, False)
        elif event.key () == Qt.Key_Right:
            self.changeColor(self.rightButton, False)

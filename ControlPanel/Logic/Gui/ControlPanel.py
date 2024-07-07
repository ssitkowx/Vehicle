from Uart                            import Uart
from Timer                           import Timer
from Labels                          import Labels
from MenuBar                         import MenuBar
from Buttons                         import Buttons
from BleComm                         import BleComm
from Settings                        import Settings
from GroupBoxes                      import GroupBoxes
from LoggerHw                        import *
from TextBrowser                     import TextBrowser
from PySide6.QtGui                   import QKeyEvent
from PySide6.QtCore                  import QSize
from CommandConverter                import CommandConverter
from PySide6.QtWidgets               import QMainWindow, QWidget
from BleParserAndSerializer          import BleParserAndSerializer
from Logic.Gui.Panels.Ble.BlePanel   import BlePanel
from Logic.Gui.Panels.Uart.UartPanel import UartPanel
from PySide6.QtCore import QTimer
class ControlPanel (QMainWindow):
    module = __name__
    
    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__ (self)
        self.labels      = Labels      ()
        self.buttons     = Buttons     ()
        self.menuBar     = MenuBar     ()
        self.textBrowser = TextBrowser ()
        self.groupBoxes  = GroupBoxes  (self.labels, self.buttons, self.textBrowser.obj)
        self.timer       = Timer       ()

        self.counter = 0

        self.buttons.clearLogs      .clicked  .connect (self.clearButtonClicked)
        self.menuBar.uartAction     .triggered.connect (self.openUartInterface)
        self.menuBar.bluetoothAction.triggered.connect (self.openBluetoothInterface)
        self.setMenuBar                                (self.menuBar.obj)
        self.timer.obj              .timeout.connect   (self.timerIsr)
        
        loggerHw = LoggerHw (self.textBrowser.obj)
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
        self.widget = QWidget (self)
        self.widget.setLayout (self.groupBoxes.obj)
        self.setCentralWidget (self.widget)

    def timerIsr (self):
        self.counter += 1
        self.labels.roll.setText (f"Roll: {self.counter}")

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
        self.textBrowser.textBrowser.clear ()

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
            char = event.text ()
            if   char == Buttons.left    : self.buttons.changeColor (self.buttons.left    , True)
            elif char == Buttons.right   : self.buttons.changeColor (self.buttons.right   , True)
            elif char == Buttons.forward : self.buttons.changeColor (self.buttons.forward , True)
            elif char == Buttons.backward: self.buttons.changeColor (self.buttons.backward, True)
            else: super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            char = event.text ()
            if   char == Buttons.left    : self.buttons.changeColor (self.buttons.left    , False)
            elif char == Buttons.right   : self.buttons.changeColor (self.buttons.right   , False)
            elif char == Buttons.forward : self.buttons.changeColor (self.buttons.forward , False)
            elif char == Buttons.backward: self.buttons.changeColor (self.buttons.backward, False)
            else: super().keyPressEvent(event)
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

        self.buttons.left           .pressed  .connect (self.leftButtonPressed)
        self.buttons.left           .released .connect (self.leftButtonReleased)
        self.buttons.right          .pressed  .connect (self.rightButtonPressed)
        self.buttons.right          .released .connect (self.rightButtonReleased)
        self.buttons.forward        .pressed  .connect (self.forwardButtonPressed)
        self.buttons.forward        .released .connect (self.forwardButtonReleased)
        self.buttons.backward       .pressed  .connect (self.backwardButtonPressed)
        self.buttons.backward       .released .connect (self.backwardButtonReleased)
        self.buttons.clearLogs      .pressed  .connect (self.clearButtonPressed)
        self.buttons.clearLogs      .released .connect (self.clearButtonReleased)
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

    def leftButtonPressed      (self): self.buttons.changeColor (self.buttons.left    , True)
    def leftButtonReleased     (self): self.buttons.changeColor (self.buttons.left    , False)
    def rightButtonPressed     (self): self.buttons.changeColor (self.buttons.right   , True)
    def rightButtonReleased    (self): self.buttons.changeColor (self.buttons.right   , False)
    def forwardButtonPressed   (self): self.buttons.changeColor (self.buttons.forward , True)
    def forwardButtonReleased  (self): self.buttons.changeColor (self.buttons.forward , False)
    def backwardButtonPressed  (self): self.buttons.changeColor (self.buttons.backward, True)
    def backwardButtonReleased (self): self.buttons.changeColor (self.buttons.backward, False)
    def clearButtonPressed (self):
        self.textBrowser.obj.clear ()
        self.buttons.changeColor   (self.buttons.clearLogs, True)

    def clearButtonReleased (self): self.buttons.changeColor (self.buttons.clearLogs, False)

    def keyPressEvent (self, event):
        if isinstance (event, QKeyEvent):
            char = event.text ()
            if   char == Buttons.left    : self.leftButtonPressed     ()
            elif char == Buttons.right   : self.rightButtonPressed    ()
            elif char == Buttons.forward : self.forwardButtonPressed  ()
            elif char == Buttons.backward: self.backwardButtonPressed ()
            else: super ().keyPressEvent (event)

    def keyReleaseEvent (self, event):
        if isinstance (event, QKeyEvent):
            char = event.text ()
            if   char == Buttons.left    : self.leftButtonReleased     ()
            elif char == Buttons.right   : self.rightButtonReleased    ()
            elif char == Buttons.forward : self.forwardButtonReleased  ()
            elif char == Buttons.backward: self.backwardButtonReleased ()
            else: super ().keyPressEvent (event)
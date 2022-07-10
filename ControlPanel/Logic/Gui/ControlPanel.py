from Uart                            import Uart
from LoggerHw                          import *
from MenuBar                         import MenuBar
from Buttons                         import Buttons
from Layouts                         import Layouts
from BleComm                         import BleComm
from Settings                        import Settings
from LineEdit                        import LineEdit
from ComboBox                        import ComboBox
from CheckBox                        import CheckBox
from TextBrowser                     import TextBrowser
from PySide6.QtCore                  import QSize
from CommandConverter                import CommandConverter
from PySide6.QtWidgets               import QMainWindow
from BleParserAndSerializer          import BleParserAndSerializer
from Logic.Gui.Panels.Ble.BlePanel   import BlePanel
from Logic.Gui.Panels.Uart.UartPanel import UartPanel
from Logger import *
class ControlPanel (QMainWindow, Buttons, MenuBar, CheckBox, ComboBox, LineEdit, TextBrowser, Layouts):
    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__ (self)
        Buttons    .__init__ (self)
        MenuBar    .__init__ (self)
        CheckBox   .__init__ (self)
        ComboBox   .__init__ (self)
        LineEdit   .__init__ (self)
        TextBrowser.__init__ (self)
        Layouts    .__init__ (self)
        
        Logger                                               (LoggerHw).SetLogging (Logger, self.textBrowser)
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

    #def LogData (self):
    #    self.textBrowser.append (str (self.uart.Receive ()))

    def CurrentIndexChanged (self, vIndex):
        self.commandLineEdit.setText (self.commandComboBox.currentText ())

    def SendButtonClicked (self, vChecked):
        data = self.commandLineEdit.text ()
        self.commandConverter.Convert (data)

        json = self.bleParserAndSerializer.serialize ()
        LOGI ("Send {0}".format (json))
        self.panel.Send         (json)

    def ConnectButtonClicked (self, vChecked):
        if (self.connectButton.text () == "Connect"):
            if self.panel.Connect () == False: return
            self.connectButton.setText ("Disconnect")
        else:
            self.panel.Disconnect ()
            self.connectButton.setText ("Connect")
            LOGW                       ("Disconnected")

    def ClearButtonClicked (self, vChecked):
        self.textBrowser.clear ()

    def OpenUartInterface (self, vChecked):
        self.uartPanel.show ()

    def OpenBluetoothInterface (self, vChecked):
        self.blePanel.show ()

    def ChooseInterface (self, vState):
        if vState == 0:
            self.panel = self.uartPanel
            self.interfaceCheckBox.setText ("To uart")
        else:
            self.panel = self.blePanel
            self.interfaceCheckBox.setText ("To bluetooth")
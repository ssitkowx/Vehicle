from Uart                   import Uart
from MenuBar                import MenuBar
from Buttons                import Buttons
from Layouts                import Layouts
from BleComm                import BleComm
from Settings               import Settings
from LineEdit               import LineEdit
from ComboBox               import ComboBox
from CheckBox               import CheckBox
from TextBrowser            import TextBrowser
from PySide6.QtCore         import QSize
from PySide6.QtWidgets      import QMainWindow
from Logic.Ble.BlePanel     import BlePanel
from Logic.Uart.UartPanel   import UartPanel
from BleParserAndSerializer import BleParserAndSerializer

class ControlPanel (QMainWindow, Buttons, MenuBar, CheckBox, ComboBox, LineEdit, TextBrowser, Layouts):
    interface = False

    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__ (self)
        Buttons    .__init__ (self)
        MenuBar    .__init__ (self)
        CheckBox   .__init__ (self)
        ComboBox   .__init__ (self)
        LineEdit   .__init__ (self)
        TextBrowser.__init__ (self)
        Layouts    .__init__ (self)
        
        self.settings               = vSettings
        self.bleParserAndSerializer = BleParserAndSerializer (self.settings)
        self.uart                   = Uart                   ()
        self.bleComm                = BleComm                ()
        self.uartPanel              = UartPanel              (self.uart)
        self.blePanel               = BlePanel               (self.bleComm, self.settings)

        self.setGeometry      (500, 200, 500, 500)
        self.setWindowTitle   ('Control Panel')
        self.setStyleSheet    ('background-color:white;'
                               'selection-color: black;'
                               'selection-background-color: gray;')
        self.setMinimumSize   (QSize(500, 500))
        self.setMaximumSize   (QSize(800, 800))
        self.setCentralWidget (self.widgetLayout)

    def LogData (self):
        self.logOutputTextBrowser.append (str (self.uart.Receive ()))

    def CurrentIndexChanged (self, vIndex):
        self.commandLineEdit.setText (self.commandComboBox.currentText ())

    def ConvertCommandToDirection (self, vCommand: str):
        if vCommand == "Move forward":
            self.settings.direction = self.settings.EMoveDirection.Forward
        elif vCommand == "Move backward":
            self.settings.direction = self.settings.EMoveDirection.Backward
        elif vCommand == "Turn left":
            self.settings.direction = self.settings.EMoveDirection.Left
        elif vCommand == "Turn right":
            self.settings.direction = self.settings.EMoveDirection.Right

    def SendButtonClicked (self, vChecked):
        data = self.commandLineEdit.text ()
        self.ConvertCommandToDirection (data)

        json = self.bleParserAndSerializer.serialize ()
        print ("Send {0}".format (json))

        if self.interface == False:
            self.uart.Send (json)
        else:
            self.bleComm.Send (json)

    def ConnectButtonClicked (self, vChecked):
        if (self.connectButton.text () == "Connect"):
            if self.interface == False:
                if self.uartPanel.Connect () == False: return
            else:
                if self.blePanel.Connect () == False: return
            self.connectButton.setText ("Disconnect")
        else:
            if self.interface == False:
                self.uart.Close (self.uartPanel.port)
            else:
                self.bleComm.Close   ()
            self.connectButton.setText ("Connect")

    def ClearButtonClicked (self, vChecked):
        self.logOutputTextBrowser.clear ()

    def OpenUartInterface (self, vChecked):
        self.uartPanel.show ()

    def OpenBluetoothInterface (self, vChecked):
        self.blePanel.show ()

    def ChooseInterface (self, vState):
        if vState == 0:
            self.interface = False
            self.interfaceCheckBox.setText ("To uart")
        else:
            self.interface = True
            self.interfaceCheckBox.setText ("To bluetooth")
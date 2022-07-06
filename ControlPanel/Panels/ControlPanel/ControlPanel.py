from Uart                            import Uart
from Settings                        import Settings
from BleClientComm                   import BleClientComm
from Panels.UartPanel                import UartPanel
from Panels.BluetoothPanel           import BluetoothPanel
from PySide6.QtCore                  import QSize
from PySide6.QtWidgets               import QMainWindow
from Panels.ControlPanel.MenuBar     import MenuBar
from Panels.ControlPanel.Buttons     import Buttons
from Panels.ControlPanel.Layouts     import Layouts
from Panels.ControlPanel.LineEdit    import LineEdit
from Panels.ControlPanel.ComboBox    import ComboBox
from Panels.ControlPanel.CheckBox    import CheckBox
from Panels.ControlPanel.TextBrowser import TextBrowser

class ControlPanel (QMainWindow, TextBrowser, Buttons, ComboBox, LineEdit, MenuBar, CheckBox, Layouts):
    interface = False

    def __init__ (self, vSettings: Settings):
        QMainWindow.__init__(self)
        TextBrowser.__init__(self)
        Buttons    .__init__(self)
        ComboBox   .__init__(self)
        LineEdit   .__init__(self)
        MenuBar    .__init__(self)
        CheckBox   .__init__(self)
        Layouts    .__init__(self)
        
        self.uart           = Uart                          ()
        self.bluetooth      = BleClientComm                 ()
        self.uartPanel      = UartPanel.UartPanel           (self.uart)
        self.bluetoothPanel = BluetoothPanel.BluetoothPanel (self.bluetooth, vSettings)

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

    def SendButtonClicked (self, vChecked):
        data = self.commandLineEdit.text ()
        print ("Send {0}".format (data))

        if self.interface == False:
            self.uart.Send (data)
        else:
            self.bluetooth.Send (data)

    def ConnectButtonClicked (self, vChecked):
        if (self.connectButton.text () == "Connect"):
            if self.interface == False:
                self.uartPanel.Connect ()
            else:
                self.bluetoothPanel.Connect ()
            self.connectButton.setText ("Disconnect")
        else:
            if self.interface == False:
                self.uart.Close (self.uartPanel.port)
            else:
                self.bluetooth.Close   ()
            self.connectButton.setText ("Connect")

    def ClearButtonClicked (self, vChecked):
        self.logOutputTextBrowser.clear ()

    def OpenUartInterface (self, vChecked):
        self.uartPanel.show ()

    def OpenBluetoothInterface (self, vChecked):
        self.bluetoothPanel.show ()

    def ChooseInterface (self, vState):
        if vState == 0:
            self.interface = False
            self.interfaceCheckBox.setText ("To uart")
        else:
            self.interface = True
            self.interfaceCheckBox.setText ("To bluetooth")
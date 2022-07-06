from Settings                       import Settings
from BleClientComm                  import BleClientComm
from PySide6.QtCore                 import QSize
from PySide6.QtWidgets              import QWidget
from Panels.BluetoothPanel.Button   import Button
from Panels.BluetoothPanel.Labels   import Labels
from Panels.BluetoothPanel.Layouts  import Layouts
from Panels.BluetoothPanel.ComboBox import ComboBox

class BluetoothPanel (QWidget, Button, ComboBox, Labels, Layouts):
    def __init__(self, vbluetooth: BleClientComm, vSettings: Settings):
        QWidget .__init__ (self)
        Button  .__init__ (self)
        ComboBox.__init__ (self)
        Labels  .__init__ (self)
        Layouts .__init__ (self)
        
        self.bluetooth = vbluetooth
        self.settings  = vSettings
        dimensions     = QSize (400, 150)

        self.setGeometry    (600, 300, dimensions.width (), dimensions.height ())
        self.setWindowTitle ('Bluetooth Panel')
        self.setStyleSheet  ('background-color:white;'
                             'selection-color: black;'
                             'selection-background-color: gray;')
        self.setFixedSize   (dimensions.width (), dimensions.height ())
        self.FillCommandComboBoxPorts ()

    def Connect (self):
        uuid    = self.uuidComboBox   .currentText ()
        address = self.addressComboBox.currentText ()
        self.FillCommandComboBoxPorts ()
        self.bluetooth.Open           (uuid, address)

    def FillCommandComboBoxPorts (self):
        self.uuidComboBox   .clear    ()
        self.addressComboBox.clear    ()
        self.uuidComboBox   .addItems (self.settings.UUID)
        self.addressComboBox.addItems (self.settings.ADDRESS)

    def SaveClicked (self, vChecked):
        self.FillCommandComboBoxPorts ()
        self.close                    ()
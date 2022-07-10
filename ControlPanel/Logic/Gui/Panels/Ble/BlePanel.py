from Panel                                 import Panel
from BleComm                               import BleComm
from Settings                              import Settings
from PySide6.QtCore                        import QSize
from PySide6.QtWidgets                     import QWidget
from Logic.Gui.Panels.Ble.Widgets.Button   import Button
from Logic.Gui.Panels.Ble.Widgets.Labels   import Labels
from Logic.Gui.Panels.Ble.Widgets.Layouts  import Layouts
from Logic.Gui.Panels.Ble.Widgets.ComboBox import ComboBox

class BlePanel (QWidget, Panel, Button, Labels, ComboBox, Layouts):
    def __init__ (self, vbleComm: BleComm, vSettings: Settings):
        QWidget .__init__ (self)
        Button  .__init__ (self)
        Labels  .__init__ (self)
        ComboBox.__init__ (self)
        Layouts .__init__ (self)
        
        self.bleComm  = vbleComm
        self.settings = vSettings
        dimensions    = QSize (400, 150)

        self.setGeometry    (600, 300, dimensions.width (), dimensions.height ())
        self.setWindowTitle ('Bluetooth Panel')
        self.setStyleSheet  ('background-color:white;'
                             'selection-color: black;'
                             'selection-background-color: gray;')
        self.setFixedSize   (dimensions.width (), dimensions.height ())
        self.FillCommandComboBoxPorts ()

    def Send (self, vJson):
        self.bleComm.Send (vJson)

    def Connect (self) -> bool:
        uuid    = self.uuidComboBox   .currentText ()
        address = self.addressComboBox.currentText ()
        self.FillCommandComboBoxPorts ()
        return self.bleComm.Open      (uuid, address)

    def Disconnect (self):
        self.bleComm.Close ()

    def FillCommandComboBoxPorts (self):
        self.uuidComboBox   .clear    ()
        self.addressComboBox.clear    ()
        self.uuidComboBox   .addItems (self.settings.UUID)
        self.addressComboBox.addItems (self.settings.ADDRESS)

    def SaveClicked (self, vChecked):
        self.FillCommandComboBoxPorts ()
        self.close                    ()

from lib2to3.pgen2.token import GREATER
from BleComm                                 import BleComm
from Settings                                import Settings
from PySide6.QtCore                          import QSize
from PySide6.QtWidgets                       import QWidget
from Logic.Gui.Panels.Ble.Widgets.Button     import Button
from Logic.Gui.Panels.Ble.Widgets.Labels     import Labels
from Logic.Gui.Panels.Ble.Widgets.Layout     import Layout
from Logic.Gui.Panels.Ble.Widgets.ComboBoxes import ComboBoxes

class BlePanel (QWidget):
    def __init__ (self, vbleComm: BleComm, vSettings: Settings):
        QWidget.__init__ (self)
        self.button     = Button     ()
        self.labels     = Labels     ()
        self.comboBoxes = ComboBoxes ()
        self.layout     = Layout     (self.labels, self.comboBoxes, self.button)
        self.bleComm    = vbleComm
        self.settings   = vSettings
        dimensions      = QSize (400, 150)

        self.button.save.clicked.connect (self.connectClicked)
        self.widget = QWidget (self)
        self.widget.setLayout (self.layout.obj)

        self.setGeometry    (600, 300, dimensions.width (), dimensions.height ())
        self.setWindowTitle ('Bluetooth Panel')
        self.setStyleSheet  ('background-color:white;'
                             'selection-color: black;'
                             'selection-background-color: gray;')
        self.setFixedSize   (dimensions.width (), dimensions.height ())
        self.__fillCommandComboBoxPorts ()

    def connect (self) -> bool:
        uuid    = self.comboBoxes.uuid   .currentText ()
        address = self.comboBoxes.address.currentText ()
        self.__fillCommandComboBoxPorts ()
        return self.bleComm.open (uuid, address)

    def disconnect (self):
        self.bleComm.close ()

    def __fillCommandComboBoxPorts (self):
        self.comboBoxes.uuid   .clear   ()
        self.comboBoxes.address.clear   ()
        self.comboBoxes.uuid   .addItem (self.settings.UUID)
        self.comboBoxes.address.addItem (self.settings.ADDRESS)

    def connectClicked (self, vChecked):
        self.__fillCommandComboBoxPorts ()
        self.close ()
        self.connect ()

import os
from   Uart                                     import Uart
from   PySide6.QtCore                           import QSize
from   PySide6.QtWidgets                        import QWidget
from   Logic.Gui.Panels.Uart.Widgets.Button     import Button
from   Logic.Gui.Panels.Uart.Widgets.Labels     import Labels
from   Logic.Gui.Panels.Uart.Widgets.Layouts    import Layouts
from   Logic.Gui.Panels.Uart.Widgets.LineEdit   import LineEdit
from   Logic.Gui.Panels.Uart.Widgets.ComboBoxes import ComboBoxes

class UartPanel (QWidget, Button, Layouts, LineEdit, ComboBoxes, Labels):
    def __init__ (self, vUart: Uart):
        QWidget   .__init__ (self)
        Button    .__init__ (self)
        Labels    .__init__ (self)
        LineEdit  .__init__ (self)
        ComboBoxes.__init__ (self)
        Layouts   .__init__ (self)
        
        self.uart  = vUart
        dimensions = QSize  (230, 300)
        self.setGeometry    (600, 300, dimensions.width (), dimensions.height ())
        self.setWindowTitle ('Uart Panel')
        self.setStyleSheet  ('background-color:white;'
                             'selection-color: black;'
                             'selection-background-color: gray;')
        self.setFixedSize   (dimensions.width (), dimensions.height ())
        self.__fillCommandComboBoxPorts ()

    def __fillCommandComboBoxPorts (self):
        self.portComboBox.clear ()
        for port in self.uart.getPortNames ():
            self.portComboBox.addItem (port)

    def send (self, vJson):
        self.uart.send (vJson)

    def connect (self) -> bool:
        self.portEnable               ()
        self.__fillCommandComboBoxPorts ()
        
        speed       = self.speedComboBox      .currentText ()
        dataBits    = self.dataBitsComboBox   .currentText ()
        stopBits    = self.stopBitsComboBox   .currentText ()
        self.port   = self.portComboBox       .currentText ()
        parityBits  = self.parityBitsComboBox .currentText ()
        flowControl = self.flowControlComboBox.currentText ()
        
        self.uart.update (self.port, speed, dataBits, stopBits, parityBits, flowControl)
        return self.uart.open (self.port)

    def disconnect (self):
        self.uart.close ()

    def connectClicked (self, vChecked):
        self.__fillCommandComboBoxPorts ()
        self.portEnable ()
        self.close ()
        self.connect ()

    def portEnable (self):
        os.system ('echo ' + self.passwordLineEdit.text () + ' | sudo -S chmod 777 /dev/' + self.portComboBox.currentText ())
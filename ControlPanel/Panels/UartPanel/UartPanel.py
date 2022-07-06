import os
from   Uart                        import Uart
from   PySide6.QtCore              import QSize
from   PySide6.QtWidgets           import QWidget
from   Panels.UartPanel.Button     import Button
from   Panels.UartPanel.Labels     import Labels
from   Panels.UartPanel.LineEdit   import LineEdit
from   Panels.UartPanel.ComboBoxes import ComboBoxes
from   Panels.UartPanel.Layouts    import Layouts

class UartPanel (QWidget, Button, ComboBoxes, Labels, LineEdit, Layouts):
    def __init__(self, vUart: Uart):
        QWidget   .__init__ (self)
        Button    .__init__ (self)
        ComboBoxes.__init__ (self)
        Labels    .__init__ (self)
        LineEdit  .__init__ (self)
        Layouts   .__init__ (self)
        
        self.uart  = vUart
        dimensions = QSize  (230, 300)
        self.setGeometry    (600, 300, dimensions.width (), dimensions.height ())
        self.setWindowTitle ('Uart Panel')
        self.setStyleSheet  ('background-color:white;'
                             'selection-color: black;'
                             'selection-background-color: gray;')
        self.setFixedSize   (dimensions.width (), dimensions.height ())
        self.FillCommandComboBoxPorts ()

    def Connect (self):
        self.PortEnable               ()
        self.FillCommandComboBoxPorts ()
        
        self.port    = self.portComboBox       .currentText ()
        speed       = self.speedComboBox      .currentText ()
        dataBits    = self.dataBitsComboBox   .currentText ()
        stopBits    = self.stopBitsComboBox   .currentText ()
        parityBits  = self.parityBitsComboBox .currentText ()
        flowControl = self.flowControlComboBox.currentText ()
        
        self.uart.Update (self.port, speed, dataBits, stopBits, parityBits, flowControl)
        self.uart.Open   (self.port)

    def FillCommandComboBoxPorts (self):
        self.portComboBox.clear ()
        for port in self.uart.GetPortNames ():
            self.portComboBox.addItem (port)

    def SaveClicked (self, vChecked):
        self.FillCommandComboBoxPorts ()
        self.PortEnable               ()
        self.close                    ()

    def PortEnable (self):
        os.system ('echo ' + self.passwordLineEdit.text () + ' | sudo -S chmod 777 /dev/' + self.portComboBox.currentText ())
import os
from   Uart                                     import Uart
from   PySide6.QtCore                           import QSize
from   PySide6.QtWidgets                        import QWidget
from   Logic.Gui.Panels.Uart.Widgets.Button     import Button
from   Logic.Gui.Panels.Uart.Widgets.Labels     import Labels
from   Logic.Gui.Panels.Uart.Widgets.Layout     import Layout
from   Logic.Gui.Panels.Uart.Widgets.LineEdit   import LineEdit
from   Logic.Gui.Panels.Uart.Widgets.ComboBoxes import ComboBoxes

class UartPanel (QWidget):
    def __init__ (self, vUart: Uart):
        QWidget.__init__ (self)
        self.button     = Button     ()
        self.labels     = Labels     ()
        self.lineEdit   = LineEdit   ()
        self.comboBoxes = ComboBoxes ()
        self.layout     = Layout     (self.labels, self.comboBoxes, self.button, self.lineEdit)

        self.button.save.clicked.connect (self.connectClicked)
        
        self.widget = QWidget (self)
        self.widget.setLayout (self.layout.obj)
        
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
        self.comboBoxes.port.clear ()
        for port in self.uart.getPortNames ():
            self.comboBoxes.port.addItem (port)

    def send (self, vMsg):
        self.uart.send (vMsg)

    def connect (self) -> bool:
        self.portEnable               ()
        self.__fillCommandComboBoxPorts ()
        
        speed       = self.comboBoxes.speed      .currentText ()
        dataBits    = self.comboBoxes.dataBits   .currentText ()
        stopBits    = self.comboBoxes.stopBits   .currentText ()
        self.port   = self.comboBoxes.port       .currentText ()
        parityBits  = self.comboBoxes.parityBits .currentText ()
        flowControl = self.comboBoxes.flowControl.currentText ()
        
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
        os.system ('echo ' + self.lineEdit.password.text () + ' | sudo -S chmod 777 /dev/' + self.comboBoxes.port.currentText ())
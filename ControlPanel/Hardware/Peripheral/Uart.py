from Logger               import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

class Uart:
    def Update (self, vPort, vSpeed, vDataBits, vStopBits, vPairtyBits, vFlowControl):
        self.serialPort = QSerialPort    ()
        self.serialPort.readyRead.connect(self.Receive)
        self.serialPort.setPortName      (vPort)
        self.serialPort.setBaudRate      (int(vSpeed))
        self.serialPort.setDataBits      (self.GetDataBits   (vDataBits))
        self.serialPort.setStopBits      (self.GetStopBits   (vStopBits))
        self.serialPort.setParity        (self.GetParityBits (vPairtyBits))
        self.serialPort.setFlowControl   (self.GetFlowControl(vFlowControl))

    def send (self, vData):
        dataLen = len (vData)
        if dataLen <= 0 or self.serialPort.isOpen () == False:
            LOGE ("Can't send data over Uart")
            return
        self.serialPort.writeData (vData, dataLen)

    def receive (self):
        return self.serialPort.readAll ()

    def getPortNames (self) -> list:
        serialPortInfo = QSerialPortInfo               ()
        portsNames     = serialPortInfo.availablePorts ()
        return [port.portName () for port in portsNames]

    def open (self, vPort) -> bool:
        if self.serialPort.open (QSerialPort.ReadWrite) == True:
            LOGI ("Connected to port: {0}".format (vPort))
            return True
        else:
            LOGE ("Can't connect to port: {0}".format (vPort))
            return False
        
    def close (self):
        self.serialPort.close ()

    def getDataBits (self, vDataBits):
        if   vDataBits == '5': return QSerialPort.Data5
        elif vDataBits == '6': return QSerialPort.Data6
        elif vDataBits == '7': return QSerialPort.Data7
        elif vDataBits == '8': return QSerialPort.Data8
        else:
            LOGE ('Unknown data bits. Expected: {0}, set: 1'.format (vDataBits))
            return QSerialPort.OneStop

    def getStopBits (self, vStopBits):
        if   vStopBits == '1'  : return QSerialPort.OneStop
        elif vStopBits == '2'  : return QSerialPort.TwoStop
        elif vStopBits == '1.5': return QSerialPort.OneAndHalfStop
        else:
            LOGE ('Unknown stop bits. Expected: {0}, set: 1'.format (vStopBits))
            return QSerialPort.OneStop

    def getParityBits (self, vParityBits):
        if   vParityBits == 'No'   : return QSerialPort.NoParity
        elif vParityBits == 'Even' : return QSerialPort.EvenParity
        elif vParityBits == 'Odd'  : return QSerialPort.OddParity
        elif vParityBits == 'Space': return QSerialPort.SpaceParity
        elif vParityBits == 'Mark' : return QSerialPort.MarkParity
        else:
            LOGE ('Unknown parity. Expected: {0}, set: No'.format (vParityBits))
            return QSerialPort.NoParity

    def getFlowControl (self, vFlowControl):
        if   vFlowControl == 'No'                : return QSerialPort.NoFlowControl
        elif vFlowControl == 'Hardware(RTS/CTS)' : return QSerialPort.HardwareControl
        elif vFlowControl == 'Software(XON/XOFF)': return QSerialPort.SoftwareControl
        else:
            LOGE ('Unknown flow control. Expected: {0}, set: No'.format (vFlowControl))
            return QSerialPort.NoFlowControl
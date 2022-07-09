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

    def Send (self, vData):
        dataLen = len (vData)
        if dataLen <= 0 or self.serialPort.isOpen () == False:
            print ("Error: Can't send data over Uart")
            return
        self.serialPort.writeData (vData, dataLen)

    def Receive (self):
        return self.serialPort.readAll ()

    def GetPortNames (self) -> list:
        serialPortInfo = QSerialPortInfo               ()
        portsNames     = serialPortInfo.availablePorts ()
        return [port.portName () for port in portsNames]

    def Open (self, vPort) -> bool:
        if self.serialPort.open (QSerialPort.ReadWrite) == True:
            print ("Success: Connected to port: {0}".format (vPort))
            return True
        else:
            print ("Error: Can't connect to port: {0}".format (vPort))
            return False
        
    def Close (self, vPort):
        self.serialPort.close ()
        print ("Error: Disconnected from port: {0}".format (vPort))

    def GetDataBits (self, vDataBits):
        if   vDataBits == '5': return QSerialPort.Data5
        elif vDataBits == '6': return QSerialPort.Data6
        elif vDataBits == '7': return QSerialPort.Data7
        elif vDataBits == '8': return QSerialPort.Data8
        else:
            print ('Error: Unknown data bits. Expected: {0}, set: 1'.format (vDataBits))
            return QSerialPort.OneStop

    def GetStopBits (self, vStopBits):
        if   vStopBits == '1'  : return QSerialPort.OneStop
        elif vStopBits == '2'  : return QSerialPort.TwoStop
        elif vStopBits == '1.5': return QSerialPort.OneAndHalfStop
        else:
            print ('Error: Unknown stop bits. Expected: {0}, set: 1'.format (vStopBits))
            return QSerialPort.OneStop

    def GetParityBits (self, vParityBits):
        if   vParityBits == 'No'   : return QSerialPort.NoParity
        elif vParityBits == 'Even' : return QSerialPort.EvenParity
        elif vParityBits == 'Odd'  : return QSerialPort.OddParity
        elif vParityBits == 'Space': return QSerialPort.SpaceParity
        elif vParityBits == 'Mark' : return QSerialPort.MarkParity
        else:
            print ('Error: Unknown parity. Expected: {0}, set: No'.format (vParityBits))
            return QSerialPort.NoParity

    def GetFlowControl (self, vFlowControl):
        if   vFlowControl == 'No'                : return QSerialPort.NoFlowControl
        elif vFlowControl == 'Hardware(RTS/CTS)' : return QSerialPort.HardwareControl
        elif vFlowControl == 'Software(XON/XOFF)': return QSerialPort.SoftwareControl
        else:
            print ('Error: Unknown flow control. Expected: {0}, set: No'.format (vFlowControl))
            return QSerialPort.NoFlowControl
import os
import bluetooth
from   Ble      import Ble
from   Rtos     import Rtos
from   Logger   import *
from   Settings import Settings

class BleComm (Ble):
    module      = __name__
    sock        = 0
    clientSock  = 0
    isConnected = False

    @staticmethod
    def isSendRunning ():
        return True
    
    @staticmethod
    def isReceiveRunning ():
        return True

    def __init__ (self, vRtos: Rtos, vSettings: Settings):
        super ().__init__ ()
        self.rtos = vRtos
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.bind               (("", bluetooth.PORT_ANY))
        self.sock.listen             (1)
        port = self.sock.getsockname ()[1]

        bluetooth.advertise_service (self.sock,
                                     "BleServer",
                                     service_id      = vSettings.UUID,
                                     service_classes = [vSettings.UUID, bluetooth.SERIAL_PORT_CLASS],
                                     profiles        = [bluetooth.SERIAL_PORT_PROFILE],
                                     # protocols=[bluetooth.OBEX_UUID]
                                    )

        LOGI (self.module, f"Waiting for connection on RFCOMM channel. Port: {port}")
        
        self.clientSock, clientInfo = self.sock.accept ()
        self.isConnected = True
        LOGI (self.module, f"Accepted connection from. Client info: {clientInfo}")

    def close (self):
        self.clientSock.close ()
        self.sock      .close ()

    def send (self, vData):
        if self.isConnected == False:
            return
        
        self.clientSock.send (vData)

    def receive (self):
        if self.isConnected == False:
            return
        
        return self.clientSock.recv (1024)
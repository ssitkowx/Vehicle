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

    def send (self, vData):
        with self.rtos.mutex:
            if self.isConnected == False:
                LOGE (self.module, "Bluetooth unconnected")
                return
        
            self.sock.send (vData)

    def isRunning (self):
        return True
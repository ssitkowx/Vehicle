import os
import bluetooth
from   Ble      import Ble
from   Logger   import *
from   Settings import Settings

class BleComm (Ble):
    sock       = 0
    clientSock = 0
    
    def __init__ (self, vSettings: Settings):
        super ().__init__ ()
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.bind                        (("", bluetooth.PORT_ANY))
        self.sock.listen                      (1)
        port      = self.sock.getsockname     ()[1]

        bluetooth.advertise_service (self.sock,
                                     "BleServer",
                                     service_id      = vSettings.UUID,
                                     service_classes = [vSettings.UUID, bluetooth.SERIAL_PORT_CLASS],
                                     profiles        = [bluetooth.SERIAL_PORT_PROFILE],
                                     # protocols=[bluetooth.OBEX_UUID]
                                    )
        
        LOGI (f"Waiting for connection on RFCOMM channel. Port: {port}")
        
        self.clientSock, clientInfo = self.sock.accept ()
        
        LOGI (f"Accepted connection from. Client info: {clientInfo}")

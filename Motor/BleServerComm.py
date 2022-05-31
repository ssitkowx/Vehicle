import bluetooth
from   Logger   import *
from   Settings import Settings

class BleServerComm:
    def __init__ (self, vSettings: Settings):
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
        
        LOGI ("Waiting for connection on RFCOMM channel", port)
        
        self.clientSock, clientInfo = self.sock.accept ()
        LOGI ("Accepted connection from", clientInfo)
        
    def __del__ (self):
        LOGI                  ("DeInit")
        self.clientSock.close ()
        self.sock      .close ()


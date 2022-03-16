from   Logger import *
import bluetooth

class BleServerComm:
    Uuid  = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    
    def __init__ (self):
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.bind                        (("", bluetooth.PORT_ANY))
        self.sock.listen                      (1)
        port      = self.sock.getsockname     ()[1]

        
        bluetooth.advertise_service (self.sock,
                                     "BleServer",
                                     service_id      = self.Uuid,
                                     service_classes = [self.Uuid, bluetooth.SERIAL_PORT_CLASS],
                                     profiles        = [bluetooth.SERIAL_PORT_PROFILE],
                                     # protocols=[bluetooth.OBEX_UUID]
                                    )
        
        print ("Waiting for connection on RFCOMM channel", port)
        
        self.clientSock, clientInfo = self.sock.accept ()
        print ("Accepted connection from", clientInfo)
        
    def __del__ (self):
        LOGI                  ("DeInit")
        self.clientSock.close ()
        self.sock      .close ()


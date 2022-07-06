from   Paths    import *
from   Ble      import Ble
from   Logger   import *
import bluetooth

class BleClientComm (Ble):
    def Open (self, vUuid: str, vAddress: str):
        serviceMatches = bluetooth.find_service (uuid = vUuid, address = vAddress)
        if len (serviceMatches) == 0:
            LOGE ("Couldn't find the BleServer service.")
            return
        
        firstMatch = serviceMatches [0]
        port       = firstMatch ["port"]
        name       = firstMatch ["name"]
        host       = firstMatch ["host"]
        
        LOGI ("Connecting to \"{0}\" on {1}".format (name, host))
        
        # Create the client socket
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.connect                     ((host, port))

    def Send (self, vData):
        self.sock.send (vData)

    def Close (self):
        self.sock.close ()

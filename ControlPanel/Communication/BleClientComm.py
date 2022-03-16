from   Paths    import *
from   Logger   import *
from   Settings import Settings  
import bluetooth 

class BleClientComm:
    def __init__ (self, vSettings: Settings):
        serviceMatches = bluetooth.find_service (uuid = vSettings.UUID, address = vSettings.ADDRESS)
        if len (serviceMatches) == 0:
            LOGE ("Couldn't find the BleServer service.")
        
        firstMatch = serviceMatches [0]
        port       = firstMatch ["port"]
        name       = firstMatch ["name"]
        host       = firstMatch ["host"]
        
        LOGI ("Connecting to \"{0}\" on {1}".format (name, host))
        
        # Create the client socket
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.connect                     ((host, port))
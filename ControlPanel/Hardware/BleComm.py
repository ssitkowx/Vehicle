import bluetooth
from   Ble    import Ble
from   Logger import *

class BleComm (Ble):
    module = __name__
    isConnected = False

    def open (self, vUuid: str, vAddress: str) -> bool:
        serviceMatches = bluetooth.find_service (uuid = vUuid, address = vAddress)
        if len (serviceMatches) == 0:
            LOGE (self.module, "Couldn't find the BleServer service.")
            return False
        
        firstMatch = serviceMatches [0]
        port       = firstMatch ["port"]
        name       = firstMatch ["name"]
        host       = firstMatch ["host"]
        
        LOGI (self.module, "Found \"{0}\" on {1}".format (name, host))
        
        # Create the client socket
        self.sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        self.sock.connect                     ((host, port))
        self.isConnected = True
        return True

    def send (self, vData):
        if self.isConnected == False:
            LOGE (self.module, "Bluetooth unconnected")
            return
        
        self.sock.send (vData)

    def close (self):
        self.isConnected = False
        self.sock.close ()

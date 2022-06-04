import os
from Logger import *

class Ble:
    def __init__ (self):
        self.enable ()
        LOGI ("Init")

    def __del__ (self):
        self.restart ()
        LOGI ("DeInit")

    def restart (self):
        os.system ('sudo systemctl restart bluetooth')

    def enable (self):
         os.system ('sudo hcitool dev')
         os.system ('sudo sdptool add SP')
         os.system ('sudo hciconfig hci0 piscan')


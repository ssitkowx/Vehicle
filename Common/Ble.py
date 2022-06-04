import os
from Logger import *

class Ble:
    def __init__ (self):
         os.system ('sudo hciconfig hci0 piscan')

    def __del__ (self):
         os.system ('sudo systemctl restart bluetooth')
         os.system ('sudo hcitool dev')
         os.system ('sudo sdptool add SP')

import os

class Ble:
    def Enable (self):
        os.system ('sudo systemctl restart bluetooth')
        os.system ('sudo hciconfig hci0 piscan')


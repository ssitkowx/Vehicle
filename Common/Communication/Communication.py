from requests       import NullHandler
from PySide6.QtCore import QByteArray

class Communication:
    def Send (self, vData) -> bool:
        return False

    def Receive (self) -> QByteArray:
        return NullHandler

    def Close (self) -> bool:
        return False
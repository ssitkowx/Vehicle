from requests import NullHandler

class Panel:
    def Connect (self) -> bool:
        return False

    def Disconnect (self):
        return NullHandler
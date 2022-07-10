from requests import NullHandler

class Panel:
    def Send (self, vJson):
        pass

    def Connect (self) -> bool:
        return False

    def Disconnect (self):
        return NullHandler
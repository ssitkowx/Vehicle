from colorama import Fore
from Logger import *

class LoggerHw (Logger):
    def __init__ (self):
        pass
    
    def log (self, vLogLevel: str, vModule: str, vMsg: str):
        msg = super ().log (vLogLevel, vModule, vMsg)
        if vLogLevel == "Debug":
            msg += Fore.BLACK
        elif vLogLevel == "Info":
            msg += Fore.BLUE
        elif vLogLevel == "Warning":
            msg += Fore.LIGHTBLACK_EX
        elif vLogLevel == "Error":
            msg += Fore.RED
        elif vLogLevel == "Critical":
            msg += Fore.MAGENTA
        print (msg)
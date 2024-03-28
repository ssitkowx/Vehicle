from Logger import *

class LoggerHw (Logger):
    def __init__ (self):
        pass
    
    def log (self, vLogLevel: str, vMsg: str):
        msg = super ().log (vLogLevel, vMsg)
        print (msg)
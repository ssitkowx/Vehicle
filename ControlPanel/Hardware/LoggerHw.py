from Logger import *

class LoggerHw (Logger):
    def __init__ (self, vTextBrowser):
        self.textBrowser = vTextBrowser
    
    def log (self, vLogLevel: str, vMsg: str):
        if vLogLevel == "Debug":
            self.textBrowser.setTextColor ("black")
        elif vLogLevel == "Info":
            self.textBrowser.setTextColor ("blue")
        elif vLogLevel == "Warning":
            self.textBrowser.setTextColor ("gray")
        elif vLogLevel == "Error":
            self.textBrowser.setTextColor ("red")
        elif vLogLevel == "Critical":
            self.textBrowser.setTextColor ("purple")
        
        msg = super ().log (vLogLevel, vMsg)
        self.textBrowser.append (msg)
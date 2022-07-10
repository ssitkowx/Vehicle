from Logger import *

class LoggerHw (Logger):
    def __new__ (self):
        if self._instance is None:
            self._instance = super (Logger, self).__new__ (self)
        return self._instance
    
    def Log (self, vLogLevel: ELogLevel, vMsg: str):
        msg = super ().Log (vLogLevel, vMsg)

        if vLogLevel == ELogLevel.Debug:
            self.textBrowser.setTextColor ("black")
        elif vLogLevel == ELogLevel.Info:
            self.textBrowser.setTextColor ("blue")
        elif vLogLevel == ELogLevel.Warning:
            self.textBrowser.setTextColor ("gray")
        elif vLogLevel == ELogLevel.Error:
            self.textBrowser.setTextColor ("red")
        elif vLogLevel == ELogLevel.Critical:
            self.textBrowser.setTextColor ("purple")

        self.textBrowser.append (msg)
from Logger import *

class LoggerHw (Logger):
    def SetLogging (self, vTextBrowser) -> None:
        self.textBrowser = vTextBrowser
    
    def Log (self, vLogLevel: ELogLevel, vMsg: str) -> None:
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

        self.textBrowser.append (vMsg)
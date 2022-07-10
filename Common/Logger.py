from enum import IntEnum

class ELogLevel (IntEnum):
    Debug    = 0
    Info     = 1
    Warning  = 2
    Error    = 3
    Critical = 4

def LOGD (vMsg: str): Logger ().Log (ELogLevel.Debug   , vMsg)
def LOGI (vMsg: str): Logger ().Log (ELogLevel.Info    , vMsg)
def LOGW (vMsg: str): Logger ().Log (ELogLevel.Warning , vMsg)
def LOGE (vMsg: str): Logger ().Log (ELogLevel.Error   , vMsg)
def LOGC (vMsg: str): Logger ().Log (ELogLevel.Critical, vMsg)

class Logger:
    _instance = None

    def SetLogger (self, vTextBrowser):
        self.textBrowser = vTextBrowser
    
    def Log (self, vLogLevel: ELogLevel, vMsg: str):
        msg = "Module: " + __name__ + ". "    #Add Module to logger

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

        self.textBrowser.append (msg + vMsg)
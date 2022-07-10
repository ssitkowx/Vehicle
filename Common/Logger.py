from enum import IntEnum
from LoggerHw import LoggerHw
class ELogLevel (IntEnum):
    Debug    = 0
    Info     = 1
    Warning  = 2
    Error    = 3
    Critical = 4

def LOGD (vMsg: str): Logger (LoggerHw).Log (Logger, ELogLevel.Debug   , vMsg)
def LOGI (vMsg: str): Logger (LoggerHw).Log (Logger, ELogLevel.Info    , vMsg)
def LOGW (vMsg: str): Logger (LoggerHw).Log (Logger, ELogLevel.Warning , vMsg)
def LOGE (vMsg: str): Logger (LoggerHw).Log (Logger, ELogLevel.Error   , vMsg)
def LOGC (vMsg: str): Logger (LoggerHw).Log (Logger, ELogLevel.Critical, vMsg)

class Logger:
    _instance = None

    def __new__ (self, vSubClass):
        if self._instance is None:
            self._instance = self
            self.subClass  = vSubClass
        return self._instance

    def SetLogging (self, vTextBrowser) -> None:
        self.subClass.SetLogging (self, vTextBrowser)
    
    def Log (self, vLogLevel: ELogLevel, vMsg: str) -> str:
        msg = "Module: " + __name__ + ". "    #Add Module to logger
        self.subClass.Log (self, vLogLevel, msg + vMsg)
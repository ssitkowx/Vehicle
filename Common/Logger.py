from abc import ABC, abstractmethod

def LOGD (vMsg: str): Logger.getInst ().log ("Debug"   , vMsg)
def LOGI (vMsg: str): Logger.getInst ().log ("Info"    , vMsg)
def LOGW (vMsg: str): Logger.getInst ().log ("Warning" , vMsg)
def LOGE (vMsg: str): Logger.getInst ().log ("Error"   , vMsg)
def LOGC (vMsg: str): Logger.getInst ().log ("Critical", vMsg)

class Logger (ABC):
    _inst = None

    def __init__ ():
        print ("Init was called unfortunatelly")

    @classmethod
    def setInst (cls, vInst):
        cls._inst = vInst

    @classmethod
    def getInst (cls):
        if cls._inst == None:
            cls._inst = cls.__new__ (cls)
        return cls._inst

    @abstractmethod
    def log (self, vLogLevel: str, vMsg: str):
        return "{0}: Module: {1}: {2}. ".format (vLogLevel, __name__, vMsg)
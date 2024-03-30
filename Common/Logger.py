from abc import ABC, abstractmethod

def LOGD (vModule: str, vMsg: str): Logger.getInst ().log ("Debug"   , vModule, vMsg)
def LOGI (vModule: str, vMsg: str): Logger.getInst ().log ("Info"    , vModule, vMsg)
def LOGW (vModule: str, vMsg: str): Logger.getInst ().log ("Warning" , vModule, vMsg)
def LOGE (vModule: str, vMsg: str): Logger.getInst ().log ("Error"   , vModule, vMsg)
def LOGC (vModule: str, vMsg: str): Logger.getInst ().log ("Critical", vModule, vMsg)

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
    def log (self, vLogLevel: str, vModule: str, vMsg: str):
        return "{0}: Module: {1}: {2}. ".format (vLogLevel, vModule, vMsg)
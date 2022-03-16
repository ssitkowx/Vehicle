import logging
from   enum import Enum

class ELogLevel (Enum):
    Debug    = logging.DEBUG
    Info     = logging.INFO
    Warning  = logging.WARNING
    Error    = logging.ERROR
    Critical = logging.CRITICAL

def LOGD (vMsg: str): logger.log (ELogLevel.Debug   , vMsg)
def LOGI (vMsg: str): logger.log (ELogLevel.Info    , vMsg)
def LOGW (vMsg: str): logger.log (ELogLevel.Warning , vMsg)
def LOGE (vMsg: str): logger.log (ELogLevel.Error   , vMsg)
def LOGC (vMsg: str): logger.log (ELogLevel.Critical, vMsg)

class Logger:
    def __init__(self):
        logging.root.setLevel (logging.NOTSET)
        
    def log (self, vLogLevel: ELogLevel, vMsg: str):
        msg = "Module: " + __name__ + ". "
        msg =  msg + vMsg
        
        if vLogLevel == ELogLevel.Debug:
            logging.debug (vMsg)
        elif vLogLevel == ELogLevel.Info:
            logging.info (vMsg)
        elif vLogLevel == ELogLevel.Warning:
            logging.warning (msg)
        elif vLogLevel == ELogLevel.Error:
            logging.error (vMsg)
        elif vLogLevel == ELogLevel.Critical:
            logging.critical (vMsg)
        else:
            print (f"Unknown log level. {vMsg}")

logger = Logger ()

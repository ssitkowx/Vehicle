import queue, threading

class Rtos:
    def __init__ (self):
        self.imuQueue = queue.Queue (maxsize=3)
        self.cmdQueue = queue.Queue (maxsize=10)
        self.imuQueue.join          ()
        self.cmdQueue.join          ()

    def createThread (self, vHandler):
        return threading.Thread (target = vHandler)
    
    def addImuQueue (self, vMsg):
        if self.imuQueue.full (): return
        self.imuQueue.put (vMsg)

    def addCmdQueue (self, vMsg):
        if self.cmdQueue.full (): return
        self.cmdQueue.put (vMsg)
    
    def getImuQueue (self):
        return self.imuQueue.get ()
    
    def getCmdQueue (self):
        return self.cmdQueue.get ()
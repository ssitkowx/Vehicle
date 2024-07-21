import queue, threading

class Rtos:
    def __init__ (self):
        self.bleMsgQueue = queue.Queue (maxsize=10)
        self.bleMsgQueue.join          ()
        self.mutex = threading.Lock    ()
    
    def addQueueMsg (self, vMsg):
        self.bleMsgQueue.put (vMsg)
    
    def getQueueMsg (self):
        return self.bleMsgQueue.get ()
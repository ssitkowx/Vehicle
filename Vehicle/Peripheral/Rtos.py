import queue, threading

class Rtos:
    def __init__ (self):
        self.bleMsgQueue = queue.Queue (maxsize=10)
        self.bleMsgQueue.join          ()
    
    def createThread (self, vHandler):
        return threading.Thread (target = vHandler, daemon = True)
    
    def addQueueMsg (self, vMsg):
        self.bleMsgQueue.put (vMsg)
    
    def getQueueMsg (self):
        return self.bleMsgQueue.get ()
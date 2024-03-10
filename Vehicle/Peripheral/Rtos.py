import queue, threading

class Rtos:
    def __init__ (self):
        self.bleMsgQueue = queue.Queue (maxsize=1)
        self.bleMsgQueue.join          ()
    
    def createThread (self, vHandler):
        return threading.Thread (target = vHandler, daemon = True)
    
    def sendMsg (self, vMsg):
        self.bleMsgQueue.put (vMsg)
    
    def getMsg (self):
        return self.bleMsgQueue.get ()
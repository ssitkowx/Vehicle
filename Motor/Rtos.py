import queue, threading

class Rtos:
    isReady = True

    def __init__ (self):
        self.bleMsgQueue = queue.Queue (maxsize=1)
        self.bleMsgQueue.join          ()
    
    def createThread (self, vHandler):
        return threading.Thread (target = vHandler, daemon = True)
    
    def sendMsg (self, vMsg):
        if self.isReady == True:
            self.isReady = False
            self.bleMsgQueue.put (vMsg)
    
    def getMsg (self):
        if self.isReady == False:
            self.isReady = True
            return self.bleMsgQueue.get ()
        return None
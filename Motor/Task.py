from   Paths                  import *
from   App                    import App
from   Rtos                   import Rtos
from   Logger                 import *
from   Settings               import Settings
from   Keyboard               import Keyboard
from   BleServerComm          import BleServerComm
from   BleParserAndSerializer import BleParserAndSerializer

class Task:
    def __init__ (self):
        self.rtos                   = Rtos                   ()
        self.settings               = Settings               ()
        self.bleParserAndSerializer = BleParserAndSerializer (self.settings)
        
        keyboardThread = self.rtos.createThread (self.keyboardProcess)
        keyboardThread .start ()
        
        #bleServerThread = self.rtos.createThread (self.bleServerProcess)
        #bleServerThread.start ()
        
        appThread      = self.rtos.createThread (self.appProcess)
        appThread      .start ()
    
        keyboardThread .join  ()
        #bleServerThread.join  ()
        appThread      .join  ()
        
    def keyboardProcess (self):
        keyboard = Keyboard (self.rtos, self.settings, self.bleParserAndSerializer)
        LOGI                ("Enter message")
'''
    def bleServerProcess (self):
        bleServerComm = BleServerComm ()
        
        try:
            while True:
                msg = self.bleServerThread.clientSock.recv (1024)
                if not msg:
                    break
                
                LOGI (f"Send: {msg}")
                self.rtos.sendMsg (msg)
        except OSError:
            pass
            
        LOGE ("Disconnected.")
'''
    def appProcess (self):
        app = App (self.settings)
        
        try:
            while True:
                msg = self.rtos.getMsg ()
                LOGI        (f"Received: {msg}")
                app.process (msg)
        except OSError:
                pass
            
        LOGE ("Disconnected.")

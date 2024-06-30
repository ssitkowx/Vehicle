import time
import rcpy
from   rcpy.motor import motor1, motor2

from   Logger     import *
from   Settings   import Settings

class App: 
    turnLeft  = False
    turnRight = False
    module    = __name__
    
    def __init__ (self, vSettings: Settings):
        self.settings = vSettings
        rcpy.set_state (rcpy.RUNNING)

    @staticmethod
    def isExiting ():
        return rcpy.get_state () == rcpy.EXITING

    @staticmethod
    def isRunning ():
        return rcpy.get_state () == rcpy.RUNNING

    @staticmethod
    def isPaused ():
        return rcpy.get_state () == rcpy.PAUSED
    
    def update (self):
        self.validate ()
        
        duty = self.settings.duty
        LOGI (self.module, f'Duty {duty}')

        if self.turnLeft == True:
            self.turnLeft = False
            motor1.set (duty)
        else:
            motor1.set (duty)
        time.sleep (0.1)
        
        if self.turnRight == True:
            self.turnRight = False
            motor2.set (duty)
        else:
            motor2.set (duty)
        time.sleep (0.1)
        
        if self.settings.brake == True:
            self.settings.brake = False
            motor1.brake ()
            motor2.brake ()
        
        if self.settings.freeSpin == True:
            self.settings.freeSpin = False
            motor1.free_spin ()
            motor2.free_spin ()
        
    def validate (self):
        topMax    = self.settings.DutyParams.RANGE ["Top"]
        bottomMax = self.settings.DutyParams.RANGE ["Bottom"]
        if self.settings.duty >= topMax:
            self.settings.duty = topMax
        
        if self.settings.duty <= bottomMax:
            self.settings.duty = bottomMax
    
    def process (self):
        if self.settings.direction == Settings.EMoveDirection.Forward:
            pass
        elif self.settings.direction == Settings.EMoveDirection.Backward:
            pass
        elif self.settings.direction == Settings.EMoveDirection.Left:
            self.turnLeft = True
        elif self.settings.direction == Settings.EMoveDirection.Right:
            self.turnRight = True
        else:
            self.settings.duty     = 0
            self.settings.freeSpin = True
        self.update ()

    @staticmethod
    def isMsgDoubled (vMsg: str):    # todo sylsit I don't remember use of this function
        if vMsg.find ("MoveDirection", 20, 40) == -1:
            return False
        return True
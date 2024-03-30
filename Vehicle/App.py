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
        LOGI (self.module, f'Duty {duty / Settings.Duty.FACTOR}')

        if self.turnLeft == True:
            self.turnLeft = False
            motor1.set ((duty - Settings.Duty.STEP) / Settings.Duty.FACTOR)
        else:
            motor1.set (duty / Settings.Duty.FACTOR)
        time.sleep (0.1)
        
        if self.turnRight == True:
            self.turnRight = False
            motor2.set ((duty - Settings.Duty.STEP) / Settings.Duty.FACTOR)
        else:
            motor2.set (duty / Settings.Duty.FACTOR)
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
        if self.settings.duty >= Settings.Duty.RANGE ["Top"]:
            self.settings.duty = Settings.Duty.RANGE ["Top"]
        
        if self.settings.duty <= Settings.Duty.RANGE ["Bottom"]:
            self.settings.duty = Settings.Duty.RANGE ["Bottom"]
    
    def process (self):
        while rcpy.get_state() != rcpy.EXITING:
            if rcpy.get_state() == rcpy.RUNNING:
                if self.settings.direction == Settings.EMoveDirection.Forward:
                    self.settings.duty += Settings.Duty.STEP
                elif self.settings.direction == Settings.EMoveDirection.Backward:
                    self.settings.duty -= Settings.Duty.STEP
                elif self.settings.direction == Settings.EMoveDirection.Left:
                    self.turnLeft = True
                elif self.settings.direction == Settings.EMoveDirection.Right:
                    self.turnRight = True
                else:
                    self.settings.duty     = 0
                    self.settings.freeSpin = True
                self.update ()

    @staticmethod
    def isMsgDoubled (vMsg: str):
        if vMsg.find ("MoveDirection", 20, 40) == -1:
            return False
        return True
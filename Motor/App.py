import time
import rcpy 
from   Logger     import *
from   Settings   import Settings
from   rcpy.motor import motor1, motor2

class App: 
    turnLeft  = False
    turnRight = False
    
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
        LOGI (f'Duty {duty / Settings.DUTY_FACTOR}')

        if self.turnLeft == True:
            self.turnLeft = False
            motor1.set ((duty - Settings.DUTY_STEP) / Settings.DUTY_FACTOR)
        else:
            motor1.set (duty / Settings.DUTY_FACTOR)
        time.sleep (0.1)
        
        if self.turnRight == True:
            self.turnRight = False
            motor2.set ((duty - Settings.DUTY_STEP) / Settings.DUTY_FACTOR)
        else:
            motor2.set (duty / Settings.DUTY_FACTOR)
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
        if self.settings.duty >= Settings.DUTY_RANGE ["Top"]:
            self.settings.duty = Settings.DUTY_RANGE ["Top"]
        
        if self.settings.duty <= Settings.DUTY_RANGE ["Bottom"]:
            self.settings.duty = Settings.DUTY_RANGE ["Bottom"]
    
    def process (self):
        if self.settings.direction == Settings.EMoveDirection.Forward:
            self.settings.duty += Settings.DUTY_STEP
        elif self.settings.direction == Settings.EMoveDirection.Backward:
            self.settings.duty -= Settings.DUTY_STEP
        elif self.settings.direction == Settings.EMoveDirection.Left:
            self.turnLeft = True
        elif self.settings.direction == Settings.EMoveDirection.Right:
            self.turnRight = True
        else:
            self.settings.duty     = 0
            self.settings.freeSpin = True
        
        self.update ()
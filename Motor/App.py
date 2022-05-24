import rcpy 
import rcpy.motor as motor
from   Logger     import *
from   Settings   import Settings

class App: 
    turnLeft  = False
    turnRight = False
    
    def __init__ (self, vSettings: Settings):
        self.settings   = vSettings
        #self.leftWheel  = Motor (1)
        #self.rightWheel = Motor (2)
        rcpy.set_state (rcpy.RUNNING)
    
    def update (self):
        self.validate ()
        
        msg = f'Duty {self.settings.duty}'
        print (msg)
        
        if self.turnLeft == True:
            self.turnLeft = False
            self.leftWheel.set (self.settings.MOTORS ["LeftWheel"], self.settings.duty - self.settings.DUTY_STEP)
        else:
            self.leftWheel.set (self.settings.MOTORS ["LeftWheel"], self.settings.duty)
           
        if self.turnLeft == True:
            self.turnLeft = False
            self.rightWheel.set (self.settings.MOTORS ["RightWheel"], self.settings.duty - self.settings.DUTY_STEP)
        else:
           self.rightWheel.set (self.settings.MOTORS ["RightWheel"], self.settings.duty)
        
        if self.settings.brake == True:
            self.settings  .brake = False
            self.leftWheel .brake (self.settings.MOTORS ["LeftWheel" ])
            self.rightWheel.brake (self.settings.MOTORS ["RightWheel"])
        
        if self.settings.freeSpin == True:
            self.settings  .freeSpin = False
            self.leftWheel .free_spin (self.settings.MOTORS ["RightWheel"])
            self.rightWheel.free_spin (self.settings.MOTORS ["LeftWheel" ])
        
    def validate (self):
        if self.settings.duty >= self.settings.DUTY_RANGE ["Top"]:
            self.settings.duty = self.settings.DUTY_RANGE ["Top"]
        
        if self.settings.duty <= self.settings.DUTY_RANGE ["Bottom"]:
            self.settings.duty = self.settings.DUTY_RANGE ["Bottom"]
    
    def process (self):
        if self.settings.direction == "EMoveDirection.Forward":
            self.settings.duty += self.settings.DUTY_STEP
        elif self.settings.direction == "EMoveDirection.Backward":
            self.settings.duty -= self.settings.DUTY_STEP
        elif self.settings.direction == "EMoveDirection.Left":
            self.turnLeft = True
        elif self.settings.direction == "EMoveDirection.Right":
            self.turnRight = True
        else:
            self.settings.duty     = 0
            self.settings.freeSpin = True
        
        self.update ()
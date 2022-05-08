import rcpy 
import rcpy.motor as motor
from   Logger     import *
from   Settings   import Settings

class App:
    duty       = 0
    brake      = False
    freeSpin   = False
    turnLeft   = False
    turnRight  = False
    
    def __init__ (self, vSettings: Settings):
        self.settings   = vSettings
        self.leftWheel  = Motor (1)
        self.rightWheel = Motor (2)
        rcpy.set_state (rcpy.RUNNING)
    
    def update (self):
        self.validate ()
        
        msg = f'Duty {self.duty}'
        print (msg)
        
        if self.turnLeft == True:
            self.turnLeft = False
            self.leftWheel.set (self.settings.MOTORS ["LeftWheel"], self.duty - self.settings.DUTY_STEP)
        else:
           self.leftWheel.set (self.settings.MOTORS ["LeftWheel"], self.duty)
           
        if self.turnLeft == True:
            self.turnLeft = False
            self.rightWheel.set (self.settings.MOTORS ["RightWheel"], self.duty - self.settings.DUTY_STEP)
        else:
           self.rightWheel .set (self.settings.MOTORS ["RightWheel"], self.duty)
        
        if self.brake == True:
            self.brake = False
            self.leftWheel .brake (self.settings.MOTORS ["LeftWheel" ])
            self.rightWheel.brake (self.settings.MOTORS ["RightWheel"])
        
        if self.freeSpin == True:
            self.freeSpin = False
            self.leftWheel .free_spin (self.settings.MOTORS ["RightWheel"])
            self.rightWheel.free_spin (self.settings.MOTORS ["LeftWheel" ])
        
    def validate (self):
        if self.duty >= self.settings.DUTY_RANGE ["Top"]:
            self.duty = self.settings.DUTY_RANGE ["Top"]
        
        if self.duty <= self.settings.DUTY_RANGE ["Bottom"]:
            self.duty = self.settings.DUTY_RANGE ["Bottom"]
    
    def process (self):
        if self.settings.direction == "EMoveDirection.Forward":
            self.duty += self.settings.DUTY_STEP
        elif self.direction == "EMoveDirection.Backward":
            self.duty -= self.settings.DUTY_STEP
        elif self.direction == "EMoveDirection.Left":
            self.turnLeft = True
        elif self.direction == "EMoveDirection.Right":
            self.turnRight = True
        else:
            self.duty     = 0
            self.freeSpin = True
        
        self.update ()
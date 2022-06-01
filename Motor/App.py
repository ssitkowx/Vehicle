import rcpy 
from   rcpy.motor import motor1, motor2
from   Settings   import Settings

class App: 
    turnLeft  = False
    turnRight = False
    
    def __init__ (self, vSettings: Settings):
        self.settings   = vSettings
        self.leftWheel  = motor1
        self.rightWheel = motor2
        rcpy.set_state (rcpy.RUNNING)
        
    def limit (self, vData: int, vTopLimit: int, vBottomLimit: int):
        if vData > vTopLimit:
            return vTopLimit
        if vData < vBottomLimit:
            return vBottomLimit
        return vData
    
    def update (self):
        self.validate ()
        
        msg = f'Duty {self.settings.duty}'
        print (msg)
        if self.turnLeft == True:
            self.turnLeft = False
            duty = self.limit (self.settings.duty - Settings.DUTY_STEP, 1, 0)
            self.leftWheel.set (duty)
        else:
            self.leftWheel.set (self.settings.duty)
            #motor1.set (self.settings.duty)
        
        if self.turnRight == True:
            self.turnRight = False
            duty = self.limit (self.settings.duty - Settings.DUTY_STEP, 1, 0)
            self.rightWheel.set (duty)
        else:
            #self.rightWheel.set (self.settings.duty)
            motor2.set (self.settings.duty)
        
        if self.settings.brake == True:
            self.settings  .brake = False
            self.leftWheel .brake ()
            self.rightWheel.brake ()
        
        if self.settings.freeSpin == True:
            self.settings  .freeSpin = False
            self.leftWheel .free_spin ()
            self.rightWheel.free_spin ()
        
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
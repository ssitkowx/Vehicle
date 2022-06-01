import rcpy 
from   rcpy.motor import motor1, motor2
from   Settings   import Settings

class App: 
    turnLeft  = False
    turnRight = False
    
    def __init__ (self, vSettings: Settings):
        self.settings   = vSettings
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
            motor1.set (duty)
        else:
            motor1.set (self.settings.duty)
        
        if self.turnRight == True:
            self.turnRight = False
            duty = self.limit (self.settings.duty - Settings.DUTY_STEP, 1, 0)
            motor2.set (duty)
        else:
            motor2.set (self.settings.duty)
        
        if self.settings.brake == True:
            self.settings  .brake = False
            motor1.brake ()
            motor2.brake ()
        
        if self.settings.freeSpin == True:
            self.settings  .freeSpin = False
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
import rcpy 
import rcpy.motor as motor
from   Logger   import *
from   Settings import Settings
class App:
    def __init__(self, vSettings: Settings):
        self.settings = vSettings
        self.leftWheel  = Motor(1)
        self.rightWheel = Motor(2)
        rcpy.set_state(rcpy.RUNNING)
    
    def update (self):
        self.validate ()
        
        self.leftWheel .set       (self.settings.motors ["LeftWheel"][0]["Duty"])
        self.leftWheel .brake     (self.settings.motors ["LeftWheel"][1]["Brake"])
        self.leftWheel .free_spin (self.settings.motors ["LeftWheel"][2]["FreeSpin"])
        
        self.rightWheel.set       (self.settings.motors ["RightWheel"][0]["Duty"])
        self.rightWheel.brake     (self.settings.motors ["RightWheel"][1]["Brake"])
        self.rightWheel.free_spin (self.settings.motors ["RightWheel"][2]["FreeSpin"])
        
    def validate (self):
        if self.settings.motors ["LeftWheel"][0]["Duty"] >= 1:
            self.settings.motors ["LeftWheel"][0]["Duty"] = 1
        
        if self.settings.motors ["RightWheel"][0]["Duty"] >= 1:
            self.settings.motors ["RightWheel"][0]["Duty"] = 1
        
        if self.settings.motors ["LeftWheel"][0]["Duty"] <= -1:
            self.settings.motors ["LeftWheel"][0]["Duty"] = -1
        
        if self.settings.motors ["RightWheel"][0]["Duty"] <= -1:
            self.settings.motors ["RightWheel"][0]["Duty"] = -1
        
    def process (self):
        if self.settings.direction == "EDirection.eForward":
            LOGI ("Move forward")
            self.settings.motors ["LeftWheel" ][0]["Duty"] = self.settings.motors ["LeftWheel" ][0]["Duty"] + 0.1
            self.settings.motors ["RightWheel"][0]["Duty"] = self.settings.motors ["RightWheel"][0]["Duty"] + 0.1
        elif self.settings.direction == "EDirection.eBackward":
            LOGI ("Move backward")
            self.settings.motors ["LeftWheel" ][0]["Duty"] = self.settings.motors ["LeftWheel" ][0]["Duty"] - 0.1
            self.settings.motors ["RightWheel"][0]["Duty"] = self.settings.motors ["RightWheel"][0]["Duty"] - 0.1
        elif self.settings.direction == "EDirection.eLeft":
            LOGI ("Move left")
            self.settings.motors ["RightWheel"][0]["Duty"] = self.settings.motors ["RightWheel"][0]["Duty"] - 0.1
        elif self.settings.direction == "EDirection.eRight":
            LOGI ("Move right")
            self.settings.motors ["LeftWheel" ][0]["Duty"] = self.settings.motors ["LeftWheel" ][0]["Duty"] - 0.1
        else:
            LOGE ("Stop")
            self.settings.motors ["LeftWheel" ][0]["Duty"] = 0
            self.settings.motors ["RightWheel"][0]["Duty"] = 0
        
        self.update ()
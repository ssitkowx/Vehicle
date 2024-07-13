import time
import rcpy
import Cmd_pb2 as CmdProto
from   rcpy.motor import motor1, motor2

from   Logger     import *
from   Settings   import Settings

class App: 
    module    = __name__
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
        
        duty = self.settings.vehicleMsg.Duty
        LOGI (self.module, f'Duty {duty}')

        if self.turnLeft == True:
            self.turnLeft = False
            motor1.set (0)
            time.sleep (Settings.Duty.TIMEOUT)
        else:
            motor1.set (duty)
        time.sleep (0.1)
        
        if self.turnRight == True:
            self.turnRight = False
            motor2.set (0)
            time.sleep (Settings.Duty.TIMEOUT)
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
        topMax    = self.settings.Duty.RANGE ["Top"]
        bottomMax = self.settings.Duty.RANGE ["Bottom"]
        if self.settings.vehicleMsg.Duty >= topMax:
            self.settings.vehicleMsg.Duty = topMax
        
        if self.settings.vehicleMsg.Duty <= bottomMax:
            self.settings.vehicleMsg.Duty = bottomMax
    
    def process (self):
        if self.settings.vehicleMsg.Direction == CmdProto.EDirection.Move:
            pass
        elif self.settings.vehicleMsg.Direction == CmdProto.EDirection.Left:
            self.turnLeft = True
        elif self.settings.vehicleMsg.Direction == CmdProto.EDirection.Right:
            self.turnRight = True
        else:
            self.settings.freeSpin        = True
            self.settings.vehicleMsg.Duty = 0
        self.update ()
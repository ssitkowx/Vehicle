import time
import rcpy
import Cmd_pb2 as CmdProto

from   Logger     import *
from   Settings   import Settings
from   rcpy.motor import motor1, motor2

class App: 
    module    = __name__
    turnLeft  = False
    turnRight = False

    @staticmethod
    def isRunning ():
        return rcpy.get_state () != rcpy.EXITING

    def __init__ (self, vSettings: Settings):
        self.settings = vSettings
        rcpy.set_state (rcpy.RUNNING)

    def update (self):
        self.validate ()
        
        duty = self.settings.vehicleMsg.Duty
        LOGI (self.module, f'Duty {duty}[%]')
        duty = (float)(duty / self.settings.Duty.DEV_COEF)

        if self.turnLeft == True:
            self.turnLeft = False
            motor1.set (duty * Settings.Duty.Timeout.TURN)
            time.sleep (Settings.Duty.Timeout.MOVE)
            motor1.set (duty)
        else:
            motor1.set (duty)
        
        if self.turnRight == True:
            self.turnRight = False
            motor2.set (duty * Settings.Duty.Timeout.TURN)
            time.sleep (Settings.Duty.Timeout.MOVE)
            motor2.set (duty)
        else:
            motor2.set (duty)
        
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
        if self.settings.vehicleMsg.Direction == CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index:
            pass
        elif self.settings.vehicleMsg.Direction == CmdProto.EDirection.DESCRIPTOR.values_by_name['Left'].index:
            self.turnLeft = True
        elif self.settings.vehicleMsg.Direction == CmdProto.EDirection.DESCRIPTOR.values_by_name['Right'].index:
            self.turnRight = True
        else:
            self.settings.freeSpin        = True
            self.settings.vehicleMsg.Duty = 0
        self.update ()
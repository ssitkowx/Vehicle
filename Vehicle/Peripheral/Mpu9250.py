import rcpy
import rcpy.mpu9250 as mpu9250

from   Imu      import *
from   Paths    import *
from   Logger   import *
from   Settings import Settings

class Mpu9250 (Imu):
    data   = 0
    module = __name__

    def __init__ (self, vSettings: Settings):
        self.data = mpu9250.initialize (enable_dmp      = True,
                                        dmp_sample_rate = 100)
        self.settings = vSettings
        
    def getAngles ():
        return mpu9250.read ()

    @staticmethod
    def isExiting ():
        return rcpy.get_state () == rcpy.EXITING

    def process (self):
        data = getAngles ()
        (self.settings.ImuAngles.X, self.settings.ImuAngles.Y, self.settings.ImuAngles.Z) = data ['quat']
        
        LOGI (self.module, 'Imu: X:{0:6}, Y:{1:6}, Z:{2:6} [deg]'.format (self.settings.ImuAngles.X,
                                                                          self.settings.ImuAngles.Y,
                                                                          self.settings.ImuAngles.Z))

import rcpy
import rcpy.mpu9250 as mpu9250

from   Paths    import *
from   Imu      import Imu
from   Logger   import *
from   Settings import Settings

class Mpu9250 (Imu):
    module = __name__
    data   = 0

    @staticmethod
    def isRunning ():
        return rcpy.get_state () != rcpy.EXITING

    def __init__ (self, vSettings: Settings):
        self.data = mpu9250.initialize (accel_fsr       = True,
                                        gyro_fsr        = True,
                                        accel_dlpf      = True,
                                        enable_dmp      = True,
                                        dmp_sample_rate = 10)
        self.settings = vSettings
        
    def getAngles (self):
        imuX, imuY, imuZ = 0, 0, 0
        
        (imuX, imuY, imuZ) = mpu9250.read () ['tb']
        return ((int)(imuX * self.RAD_TO_DEG), (int)(imuY * self.RAD_TO_DEG), (int)(imuZ * self.RAD_TO_DEG))

    def process (self):
        [self.settings.imuAnglesMsg.Roll,
         self.settings.imuAnglesMsg.Pitch,
         self.settings.imuAnglesMsg.Yaw] = self.getAngles ()
        
        #LOGI (self.module, 'Imu: x:{0:1}, y:{1:1}, z:{2:1} [deg]'.format (round (self.settings.imuAnglesMsg.Roll , 1),
        #                                                                  round (self.settings.imuAnglesMsg.Pitch, 1),
        #                                                                  round (self.settings.imuAnglesMsg.Yaw  , 1)))

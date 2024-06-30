import rcpy
import rcpy.mpu9250 as mpu9250

from   Paths    import *
from   Imu      import Imu
from   Logger   import *
from   Settings import Settings

class Mpu9250 (Imu):
    data   = 0
    module = __name__

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
        return (imuX * self.RAD_TO_DEG, imuY * self.RAD_TO_DEG, imuZ * self.RAD_TO_DEG)

    @staticmethod
    def isExiting ():
        return rcpy.get_state () == rcpy.EXITING

    def process (self):
        angles = self.getAngles ()
        
        LOGI (self.module, 'Imu: x:{0:1}, y:{1:1}, z:{2:1} [deg]'.format (round (angles [0], 1),
                                                                          round (angles [1], 1),
                                                                          round (angles [2], 1)))

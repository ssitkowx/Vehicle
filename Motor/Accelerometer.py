import rcpy
import rcpy.mpu9250 as mpu9250
from   Paths        import *
from   Logger       import *
from   Settings     import Settings

class Accelerometer:
    data = 0
    def __init__ (self, vSettings: Settings):
        self.data = mpu9250.initialize (enable_dmp=True,
                                        dmp_sample_rate=100)
        self.settings = vSettings

    @staticmethod
    def isExiting ():
        return rcpy.get_state () == rcpy.EXITING

    def process (self):
        data = mpu9250.read ()
        (self.settings.accelerometerX, self.settings.accelerometerY, self.settings.accelerometerZ) = data ['accel']
        LOGI ('X:{0:6.2f}, Y:{1:6.2f}, Z:{2:6.2f}'.format (self.settings.accelerometerX,
                                                           self.settings.accelerometerY,
                                                           self.settings.accelerometerZ))

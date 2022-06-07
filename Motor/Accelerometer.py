import rcpy
import rcpy.mpu9250 as mpu9250
from   Logger import *

class Accelerometer:
    data = 0
    def __init__ (self):
        self.data = mpu9250.initialize (enable_dmp=True,
                                        mp_sample_rate=1000)

    @staticmethod
    def isExiting ():
        return rcpy.get_state () == rcpy.EXITING

    def process (self):
        data = mpu9250.read ()
        #data = {'accel': [9, 8, 4]}
        LOGI ('{0[0]:6.2f} {0[1]:6.2f} {0[2]:6.2f}'.format (data ['accel']))

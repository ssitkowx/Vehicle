from abc import ABC, abstractmethod

class Imu:
    RAD_TO_DEG = (180 / 3.14)
    
    def __init__ (self):
        pass
    
    @abstractmethod
    def process (self):
        pass
    
    @abstractmethod
    def getAngles (self):
        pass
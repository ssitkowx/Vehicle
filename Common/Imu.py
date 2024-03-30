from abc import ABC, abstractmethod

class Imu:
    @abstractmethod
    def process ():
        pass
    
    @abstractmethod
    def getAngles ():
        pass
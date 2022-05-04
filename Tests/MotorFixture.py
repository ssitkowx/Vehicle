import unittest
from   unittest import mock
from   mock     import MagicMock
from requests   import NullHandler
from MotorPaths import *

sys.modules ['rcpy']       = mock.MagicMock ()
sys.modules ['bluetooth']  = mock.MagicMock ()
sys.modules ['rcpy.motor'] = mock.MagicMock ()
sys.modules ['bluetooth']  = mock.MagicMock ()

from App           import App
from Task          import Task
from Settings      import Settings
from BleServerComm import BleServerComm

class MotorMock:
    def __init__ (self, number: int):
        pass
    
    def set (self, vDuty: int):
        pass
    
    def brake (self, vIsBrake: bool):
        pass
    
    def free_spin (self, visFreeSpin: bool):
        pass

class MotorFixture (unittest.TestCase):
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.Motor'                           , MotorMock, create=True)
    def setUp (self, vBleInitMock, vBleInitDel, vClientSockMock) -> None:
        vClientSockMock.recv.return_value = '{"Direction": "EDirection.eStop", "Speed": -0.1}'
        self.task = Task ()
        return super ().setUp ()
    
    def testMotorProcess (self):
        pass

    def tearDown (self) -> None:
        return super().tearDown()

if __name__ == "__main__":
    unittest.main ()
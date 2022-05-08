import unittest
from   unittest   import mock
from   MotorPaths import *

sys.modules ['rcpy']       = mock.MagicMock ()
sys.modules ['bluetooth']  = mock.MagicMock ()
sys.modules ['rcpy.motor'] = mock.MagicMock ()
sys.modules ['bluetooth']  = mock.MagicMock ()

from App           import App
from Task          import Task
from Logger        import *
from Settings      import Settings
from BleServerComm import BleServerComm

class MotorMock:
    def __init__ (self, number: int):
        pass
    
    def set (self, vChannel: int, vDuty: int):
        pass
    
    def brake (self, vChannel: int):
        pass
    
    def free_spin (self, vChannel: int):
        pass

class MotorFixture (unittest.TestCase):
    def setUp (self) -> None:
        LOGI ("MotorFixture")
        return super ().setUp ()

    @mock.patch ('Task.Task.isAppProcessRunning'       , side_effect=[True, True, True, False])
    @mock.patch ('Task.Task.isBleServerProcessRunning' , side_effect=[True, True, True, False])
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.Motor', MotorMock, create=True)
    def MoveForward (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveForward")
        vClientSockMock.recv.return_value = '{"MoveDirection": "EMoveDirection.Forward"}'
        task = Task ()
        vClientSockMock.recv.assert_called ()
        pass

    def tearDown (self) -> None:
        return super().tearDown ()
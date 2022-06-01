import unittest
from   unittest   import mock
from   defer      import return_value
from   MotorPaths import *
from   itertools  import repeat

sys.modules ['rcpy'      ] = mock.MagicMock ()
sys.modules ['bluetooth' ] = mock.MagicMock ()
sys.modules ['rcpy.motor'] = mock.MagicMock ()

from App      import App
from Task     import Task
from Logger   import *
from Settings import Settings

class MotorFixture (unittest.TestCase):
    @classmethod
    @mock.patch ('Task.Task.isAppProcessRunning'         , return_value=False)
    @mock.patch ('Task.Task.isBleServerProcessRunning'   , return_value=False)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    @mock.patch ('BleServerComm.BleServerComm.__del__'   , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    def setUpClass (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MotorFixture")
        self.task = Task ()
    
    @mock.patch ('Task.Task.isAppProcessRunning'         , side_effect=([True, False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning'   , side_effect=([True, False]))
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    @mock.patch ('BleServerComm.BleServerComm.__del__'   , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    def MoveLeftUntilMaxSpeedLimit (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveLeftUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 2}'
        self.task.settings.duty = 1
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (0.95)
        self.task.app.rightWheel.set.assert_called_with (1)
    
    @mock.patch ('Task.Task.isAppProcessRunning'         , side_effect=([True, False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning'   , side_effect=([True, False]))
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    @mock.patch ('BleServerComm.BleServerComm.__del__'   , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    def MoveRightUntilMaxSpeedLimit (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveRightUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 3}'
        self.task.settings.duty = 1
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (1)
        self.task.app.rightWheel.set.assert_called_with (0.95)

    @mock.patch ('Task.Task.isAppProcessRunning'         , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning'   , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    @mock.patch ('BleServerComm.BleServerComm.__del__'   , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    def MoveForwardUntilMaxSpeedLimit (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveForwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 0}'
        self.task.settings.duty = 0
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (1)
        self.task.app.rightWheel.set.assert_called_with (1)
        self.assertEqual                                (self.task.settings.duty, 1, "Incorrect duty cycle")
        
    @mock.patch ('Task.Task.isAppProcessRunning'         , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning'   , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    @mock.patch ('BleServerComm.BleServerComm.__del__'   , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    def MoveBackwardUntilMaxSpeedLimit (self, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveBackwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 1}'
        self.task.settings.duty = 0
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (-1)
        self.task.app.rightWheel.set.assert_called_with (-1)
        self.assertEqual                                (self.task.settings.duty, -1, "Incorrect() duty cycle")
    
    def tearDown (self) -> None:
        return super().tearDown ()
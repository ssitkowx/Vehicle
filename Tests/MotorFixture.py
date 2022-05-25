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

class MotorMock:
    def __init__ (self, number: int):
        pass
    
    def set (vChannel: int, vDuty: int):
        pass
    
    def brake (vChannel: int):
        pass
    
    def free_spin (vChannel: int):
        pass

class MotorFixture (unittest.TestCase):
    @classmethod
    @mock.patch ('Task.Task.isAppProcessRunning'       , return_value=False)
    @mock.patch ('Task.Task.isBleServerProcessRunning' , return_value=False)
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.App.leftWheel'                   , return_value=MotorMock, create=True)
    @mock.patch ('App.App.rightWheel'                  , return_value=MotorMock, create=True)
    def setUpClass (self, vMockAppRightWheel, vMockAppLeftWheel, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MotorFixture")
        self.task = Task ()
    
    @mock.patch ('Task.Task.isAppProcessRunning'       , side_effect=([True, False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning' , side_effect=([True, False]))
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.App.leftWheel'                   , return_value=MotorMock, create=True)
    @mock.patch ('App.App.rightWheel'                  , return_value=MotorMock, create=True)
    def MoveLeftUntilMaxSpeedLimit (self, vMockAppRightWheel, vMockAppLeftWheel, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveLeftUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": "EMoveDirection.Left"}'
        self.task.settings.duty = 1
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (Settings.EChannel.One, 0.95)
        self.task.app.rightWheel.set.assert_called_with (Settings.EChannel.Two, 1)
    
    @mock.patch ('Task.Task.isAppProcessRunning'       , side_effect=([True, False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning' , side_effect=([True, False]))
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.App.leftWheel'                   , return_value=MotorMock, create=True)
    @mock.patch ('App.App.rightWheel'                  , return_value=MotorMock, create=True)
    def MoveRightUntilMaxSpeedLimit (self, vMockAppRightWheel, vMockAppLeftWheel, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveRightUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": "EMoveDirection.Right"}'
        self.task.settings.duty = 1
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (Settings.EChannel.One, 1)
        self.task.app.rightWheel.set.assert_called_with (Settings.EChannel.Two, 0.95)

    @mock.patch ('Task.Task.isAppProcessRunning'       , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning' , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.App.leftWheel'                   , return_value=MotorMock, create=True)
    @mock.patch ('App.App.rightWheel'                  , return_value=MotorMock, create=True)
    def MoveForwardUntilMaxSpeedLimit (self, vMockAppRightWheel, vMockAppLeftWheel, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveForwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": "EMoveDirection.Forward"}'
        self.task.settings.duty = 0
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (Settings.EChannel.One, 1)
        self.task.app.rightWheel.set.assert_called_with (Settings.EChannel.Two, 1)
        self.assertEqual                                (self.task.settings.duty, 1, "Incorrect duty cycle")
        
    @mock.patch ('Task.Task.isAppProcessRunning'       , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Task.Task.isBleServerProcessRunning' , side_effect=([True for i in range (20)] + [False]))
    @mock.patch ('Rtos.threading.Thread.clientSock'    , create=True)
    @mock.patch ('BleServerComm.BleServerComm.__del__' , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.__init__', return_value=None)
    @mock.patch ('App.App.leftWheel'                   , return_value=MotorMock, create=True)
    @mock.patch ('App.App.rightWheel'                  , return_value=MotorMock, create=True)
    def MoveBackwardUntilMaxSpeedLimit (self, vMockAppRightWheel, vMockAppLeftWheel, vBleInitMock, vBleDelMock, vClientSockMock, isBleServerProcessRunningMock, isAppProcessRunningMock):
        LOGI ("MoveBackwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": "EMoveDirection.Backward"}'
        self.task.settings.duty = 0
        self.task.__init__                              ()
        vClientSockMock.recv.assert_called              ()
        self.task.app.leftWheel .set.assert_called_with (Settings.EChannel.One, -1)
        self.task.app.rightWheel.set.assert_called_with (Settings.EChannel.Two, -1)
        self.assertEqual                                (self.task.settings.duty, -1, "Incorrect() duty cycle")
    
    def tearDown (self) -> None:
        return super().tearDown ()
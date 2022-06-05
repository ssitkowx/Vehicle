import unittest
from   MotorPaths import *
from   unittest   import mock

sys.modules ['rcpy'      ] = mock.MagicMock ()
sys.modules ['bluetooth' ] = mock.MagicMock ()
sys.modules ['rcpy.motor'] = mock.MagicMock ()

from App      import App
from Task     import Task
from Logger   import *
from Settings import Settings

class MotorFixture (unittest.TestCase):
    @classmethod
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , return_value=False)
    @mock.patch ('App.App.isExiting'                     , return_value=True)
    @mock.patch ('Task.Task.isBleProcessRunning'         , return_value=False)
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    def setUpClass (self, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMockSleep):
        LOGI ("MotorFixture")
        self.task = Task ()

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Task.Task.isBleProcessRunning'         , side_effect =[True, False])
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    def moveLeftUntilMaxSpeedLimit (self, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveLeftUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 2}'
        self.task.settings.duty           = 10
        self.task.__init__                 ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (0.9)
        vMotor2.set.assert_called_with     (1)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Task.Task.isBleProcessRunning'         , side_effect =[True, False])
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    def moveRightUntilMaxSpeedLimit (self, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveRightUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 3}'
        self.task.settings.duty           = 10
        self.task.__init__                 ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (1)
        vMotor2.set.assert_called_with     (0.9)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('App.App.isExiting'                     , side_effect=([False for i in range (10)] + [True]))
    @mock.patch ('Task.Task.isBleProcessRunning'         , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    def moveForwardUntilMaxSpeedLimit (self, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveForwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 0}'
        self.task.settings.duty           = 0
        self.task.__init__                 ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (1)
        vMotor2.set.assert_called_with     (1)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('App.App.isExiting'                     , side_effect=([False for i in range (10)] + [True]))
    @mock.patch ('Task.Task.isBleProcessRunning'         , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('BleServerComm.BleServerComm.__init__'  , return_value=None)
    @mock.patch ('BleServerComm.BleServerComm.clientSock')
    def moveBackwardUntilMaxSpeedLimit (self, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveBackwardUntilMaxSpeedLimit")
        vClientSockMock.recv.return_value = '{"MoveDirection": 1}'
        self.task.settings.duty           = 0
        self.task.__init__                 ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (-1)
        vMotor2.set.assert_called_with     (-1)

    def tearDown (self) -> None:
        return super().tearDown ()
    
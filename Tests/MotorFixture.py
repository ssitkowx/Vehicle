import unittest
from   Paths    import *
from   unittest import mock

sys.modules ['rcpy'        ] = mock.MagicMock ()
sys.modules ['bluetooth'   ] = mock.MagicMock ()
sys.modules ['rcpy.motor'  ] = mock.MagicMock ()
sys.modules ['rcpy.mpu9250'] = mock.MagicMock ()

from App           import App
from Logger        import *
from Process       import Process
from Settings      import Settings
from Accelerometer import Accelerometer

class MotorFixture (unittest.TestCase):
    @classmethod
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , return_value=False)
    @mock.patch ('App.App.isExiting'                     , return_value=True)
    @mock.patch ('Process.Process.isBleProcessRunning'   , return_value=False)
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Accelerometer.Accelerometer.isExiting' , return_value=True)
    def setUpClass (self, vIsAccelerometerExitingMock, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMockSleep):
        LOGI ("MotorFixture")
        self.process = Process ()

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect =[True, False])
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Accelerometer.Accelerometer.isExiting' , side_effect =[False, True])
    @mock.patch ('Accelerometer.mpu9250'   )
    def moveLeftUntilMaxSpeedLimit (self, vMpu9250Mock, vIsAccelerometerExitingMock, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveLeftUntilMaxSpeedLimit")
        vMpu9250Mock.read.return_value    = {'accel': [10, -10, 5], 'gyro': [10, -10, 5]}
        vClientSockMock.recv.return_value = b'{"MoveDirection": 2}'
        self.process.settings.duty        = 10
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (0.9)
        vMotor2.set.assert_called_with     (1)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect =[True, False])
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Accelerometer.Accelerometer.isExiting' , side_effect =[False, True])
    @mock.patch ('Accelerometer.mpu9250'   )
    def moveRightUntilMaxSpeedLimit (self, vMpu9250Mock, vIsAccelerometerExitingMock, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveRightUntilMaxSpeedLimit")
        vMpu9250Mock.read.return_value    = {'accel': [10, -10, 5], 'gyro': [10, -10, 5]}
        vClientSockMock.recv.return_value = b'{"MoveDirection": 3}'
        self.process.settings.duty        = 10
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (1)
        vMotor2.set.assert_called_with     (0.9)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('App.App.isExiting'                     , side_effect=([False for i in range (10)] + [True]))
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Accelerometer.Accelerometer.isExiting' , side_effect =[False, True])
    @mock.patch ('Accelerometer.mpu9250'   )
    def moveForwardUntilMaxSpeedLimit (self, vMpu9250Mock, vIsAccelerometerExitingMock, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveForwardUntilMaxSpeedLimit")
        vMpu9250Mock.read.return_value    = {'accel': [10, -10, 5], 'gyro': [10, -10, 5]}
        vClientSockMock.recv.return_value = b'{"MoveDirection": 3}'
        vClientSockMock.recv.return_value = b'{"MoveDirection": 0}'
        self.process.settings.duty        = 0
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (1)
        vMotor2.set.assert_called_with     (1)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('App.App.isExiting'                     , side_effect=([False for i in range (10)] + [True]))
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect=([True  for i in range (10)] + [False]))
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Accelerometer.Accelerometer.isExiting' , side_effect =[False, True])
    @mock.patch ('Accelerometer.mpu9250'   )
    def moveBackwardUntilMaxSpeedLimit (self, vMpu9250Mock, vIsAccelerometerExitingMock, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock, vIsExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI ("moveBackwardUntilMaxSpeedLimit")
        vMpu9250Mock.read.return_value    = {'accel': [10, -10, 5], 'gyro': [10, -10, 5]}
        vClientSockMock.recv.return_value = b'{"MoveDirection": 3}'
        vClientSockMock.recv.return_value = b'{"MoveDirection": 1}'
        self.process.settings.duty        = 0
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (-1)
        vMotor2.set.assert_called_with     (-1)

    def tearDown (self) -> None:
        return super().tearDown ()
    
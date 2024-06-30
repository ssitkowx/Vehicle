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

class MotorFixture (unittest.TestCase):
    module = __name__
    
    @classmethod
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , return_value=False)
    @mock.patch ('App.App.isExiting'                     , return_value=True)
    @mock.patch ('Process.Process.isBleProcessRunning'   , return_value=False)
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Mpu9250.Mpu9250.isExiting'             , side_effect=[True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'             , return_value=[90, -90, 90])
    def setUpClass (self, vMockGetAngles, vMockIsExisting, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock,
                          vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMockSleep):
        LOGI (self.module, "MotorFixture")
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
    @mock.patch ('Mpu9250.Mpu9250.isExiting'             , side_effect=[False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'             , return_value=[90, -90, 90])
    def moveForwardWithDuty (self, vMockGetAngles, vMockIsExisting, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock,
                                   vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI (self.module, "moveForwardWithDuty")
        vClientSockMock.recv.return_value = b'{"Duty": 0.8, "MoveDirection": 0}'
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (0.8)
        vMotor2.set.assert_called_with     (0.8)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect =[True, False])
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Mpu9250.Mpu9250.isExiting'             , side_effect=[False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'             , return_value=[80, -70, 60])
    def moveBackwardWithDuty (self, vMockGetAngles, vMockIsExisting, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock,
                                    vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI (self.module, "moveBackwardWithDuty")
        vClientSockMock.recv.return_value = b'{"Duty": 0.2, "MoveDirection": 1}'
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (0.2)
        vMotor2.set.assert_called_with     (0.2)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect =[True, False])
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Mpu9250.Mpu9250.isExiting'             , side_effect=[False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'             , return_value=[90, -90, 90])
    def turnLeft (self, vMockGetAngles, vMockIsExisting, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock,
                        vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI (self.module, "turnLeft")
        vClientSockMock.recv.return_value = b'{"Duty": 0.1, "MoveDirection": 2}'
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.set.assert_called_with     (0.1)
        vMotor2.assert_not_called          ()

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                            , create=True)
    @mock.patch ('App.motor2'                            , create=True)
    @mock.patch ('App.App.isPaused'                      , return_value=False)
    @mock.patch ('App.App.isRunning'                     , side_effect =[True, False])
    @mock.patch ('App.App.isExiting'                     , side_effect =[False, True])
    @mock.patch ('Process.Process.isBleProcessRunning'   , side_effect =[True, False])
    @mock.patch ('BleComm.BleComm.__init__'              , return_value=None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('Mpu9250.Mpu9250.isExiting'             , side_effect=[False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'             , return_value=[90, -90, 90])
    def turnRight (self, vMockGetAngles, vMockIsExisting, vClientSockMock, vBleInitMock, vIsBleProcessRunningMock,
                        vIsAppExitingMock, vIsRunningMock, vIsPausedMock, vMotor2, vMotor1, vMockSleep):
        LOGI (self.module, "turnRight")
        vClientSockMock.recv.return_value = b'{"Duty": 0.2, "MoveDirection": 3}'
        self.process.settings.duty = 0.4
        self.process.__init__              ()
        vClientSockMock.recv.assert_called ()
        vMotor1.assert_not_called          ()
        vMotor2.set.assert_called_with     (0.2)

    def tearDown (self) -> None:
        return super().tearDown ()
    
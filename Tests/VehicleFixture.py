import unittest
from   Paths    import *
from   unittest import mock

sys.modules ['rcpy'        ] = mock.MagicMock ()
sys.modules ['bluetooth'   ] = mock.MagicMock ()
sys.modules ['rcpy.motor'  ] = mock.MagicMock ()
sys.modules ['rcpy.mpu9250'] = mock.MagicMock ()

from App      import App
from Logger   import *
from Process  import Process
from Settings import Settings

def zonk ():
    return [0,0]

class VehicleFixture (unittest.TestCase):
    module = __name__

    @classmethod
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.App.isPaused'         , return_value = False)
    @mock.patch ('App.App.isRunning'        , return_value = False)
    @mock.patch ('App.App.isExiting'        , return_value = True)
    @mock.patch ('BleComm.BleComm.__init__' , return_value = None)
    @mock.patch ('BleComm.BleComm.isRunning', return_value = False)
    @mock.patch ('Mpu9250.Mpu9250.isExiting', side_effect  = [True, False])
    def setUpClass (self, vIsExistingInMpu9250, vInitInBleComm, vIsRunningInBleComm,
                          vIsExitingInApp, vIsRunningInApp, vIsPausedInApp, vSleepInApp):
        LOGI (self.module, "MotorFixture")
        self.process = Process ()

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                 , create       = True)
    @mock.patch ('App.motor2'                 , create       = True)
    @mock.patch ('App.App.isPaused'           , return_value = False)
    @mock.patch ('App.App.isRunning'          , side_effect  = [True, True])
    @mock.patch ('App.App.isExiting'          , side_effect  = [False, False, True])
    @mock.patch ('BleComm.BleComm.__init__'   , return_value = None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('BleComm.BleComm.sock'       , return_value = [0, 0])
    @mock.patch ('BleComm.BleComm.rtos'       , create       = True)
    @mock.patch ('BleComm.BleComm.isRunning'  , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isConnected', return_value = True)
    @mock.patch ('Mpu9250.Mpu9250.isExiting'  , side_effect  = [False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'  , return_value = [10, -70, 60])
    def moveForwardWithDuty (self, vMockGetAngles, vIsExistingInBleComm, vIsConnectedInBleComm, 
                                   vIsRunningInBleComm, vRtosInBleComm, vSockInBleComm, vClientSockInBleComm,
                                   vInitInBleComm, vIsAppExitingInApp, vIsRunningInApp, vIsPausedInApp,
                                   vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "moveForwardWithDuty")
        serializedImu        = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedForwardMsg = b'\n\x04\x08d\x10\x02'
        vClientSockInBleComm.recv.return_value = serializedForwardMsg

        self.process.__init__ ()
        vClientSockInBleComm.recv.assert_called     ()
        vMotor1             .set.assert_called_with (1)
        vMotor2             .set.assert_called_with (1)
        #vSockInBleComm      .send.assert_any_call   (serializedForwardMsg)
        #vSockInBleComm      .send.assert_any_call   (serializedImu)
    
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                 , create       = True)
    @mock.patch ('App.motor2'                 , create       = True)
    @mock.patch ('App.App.isPaused'           , return_value = False)
    @mock.patch ('App.App.isRunning'          , side_effect  = [True, True])
    @mock.patch ('App.App.isExiting'          , side_effect  = [False, False, True])
    @mock.patch ('BleComm.BleComm.__init__'   , return_value = None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('BleComm.BleComm.sock'       , return_value = [0, 0])
    @mock.patch ('BleComm.BleComm.rtos'       , create       = True)
    @mock.patch ('BleComm.BleComm.isRunning'  , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isConnected', return_value = True)
    @mock.patch ('Mpu9250.Mpu9250.isExiting'  , side_effect  = [False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'  , return_value = [10, -70, 60])
    def moveBackwardWithDuty (self, vMockGetAngles, vIsExistingInBleComm, vIsConnectedInBleComm, 
                                    vIsRunningInBleComm, vRtosInBleComm, vSockInBleComm, vClientSockInBleComm,
                                    vInitInBleComm, vIsAppExitingInApp, vIsRunningInApp, vIsPausedInApp,
                                    vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "moveBackwardWithDuty")
        serializedImu         = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedBackwardMsg = b'\n\r\x08\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x02'
        vClientSockInBleComm.recv.return_value = serializedBackwardMsg

        self.process.__init__ ()
        vClientSockInBleComm.recv.assert_called     ()
        vMotor1             .set.assert_called_with (-1)
        vMotor2             .set.assert_called_with (-1)
        #vSockInBleComm      .send.assert_any_call   (serializedBackwardMsg)
        #vSockInBleComm      .send.assert_any_call   (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                 , create       = True)
    @mock.patch ('App.motor2'                 , create       = True)
    @mock.patch ('App.App.isPaused'           , return_value = False)
    @mock.patch ('App.App.isRunning'          , side_effect  = [True, True])
    @mock.patch ('App.App.isExiting'          , side_effect  = [False, False, True])
    @mock.patch ('BleComm.BleComm.__init__'   , return_value = None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('BleComm.BleComm.sock'       , return_value = [0, 0])
    @mock.patch ('BleComm.BleComm.rtos'       , create       = True)
    @mock.patch ('BleComm.BleComm.isRunning'  , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isConnected', return_value = True)
    @mock.patch ('Mpu9250.Mpu9250.isExiting'  , side_effect  = [False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'  , return_value = [10, -70, 60])
    def turnLeft (self, vMockGetAngles, vIsExistingInBleComm, vIsConnectedInBleComm, 
                        vIsRunningInBleComm, vRtosInBleComm, vSockInBleComm, vClientSockInBleComm,
                        vInitInBleComm, vIsAppExitingInApp, vIsRunningInApp, vIsPausedInApp,
                        vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "turnLeft")
        serializedImu         = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedTurnLeftMsg = b'\n\x04\x082\x10\x03'
        vClientSockInBleComm.recv.return_value = serializedTurnLeftMsg

        self.process.__init__ ()
        vClientSockInBleComm.recv.assert_called   ()
        vMotor1             .set.assert_any_call  (0)
        vMotor1             .set.assert_any_call  (0.5)
        vMotor2             .set.assert_any_call  (0.5)
        #vSockInBleComm      .send.assert_any_call (serializedTurnLeftMsg)
        #vSockInBleComm      .send.assert_any_call (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                 , create       = True)
    @mock.patch ('App.motor2'                 , create       = True)
    @mock.patch ('App.App.isPaused'           , return_value = False)
    @mock.patch ('App.App.isRunning'          , side_effect  = [True, True])
    @mock.patch ('App.App.isExiting'          , side_effect  = [False, False, True])
    @mock.patch ('BleComm.BleComm.__init__'   , return_value = None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('BleComm.BleComm.sock'       , return_value = [0, 0])
    @mock.patch ('BleComm.BleComm.rtos'       , create       = True)
    @mock.patch ('BleComm.BleComm.isRunning'  , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isConnected', return_value = True)
    @mock.patch ('Mpu9250.Mpu9250.isExiting'  , side_effect  = [False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'  , return_value = [10, -70, 60])
    def turnRight (self, vMockGetAngles, vIsExistingInBleComm, vIsConnectedInBleComm, 
                         vIsRunningInBleComm, vRtosInBleComm, vSockInBleComm, vClientSockInBleComm,
                         vInitInBleComm, vIsAppExitingInApp, vIsRunningInApp, vIsPausedInApp,
                         vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "turnRight")
        serializedImu          = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedTurnRightMsg = b'\n\r\x08\xce\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x04'
        vClientSockInBleComm.recv.return_value = serializedTurnRightMsg

        self.process.__init__ ()
        vClientSockInBleComm.recv.assert_called   ()
        vMotor1             .set.assert_any_call  (-0.5)
        vMotor2             .set.assert_any_call  (0)
        vMotor2             .set.assert_any_call  (-0.5)
        #vSockInBleComm      .send.assert_any_call (serializedTurnRightMsg)
        #vSockInBleComm      .send.assert_any_call (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                 , create       = True)
    @mock.patch ('App.motor2'                 , create       = True)
    @mock.patch ('App.App.isPaused'           , return_value = False)
    @mock.patch ('App.App.isRunning'          , side_effect  = [True, True])
    @mock.patch ('App.App.isExiting'          , side_effect  = [False, True])
    @mock.patch ('BleComm.BleComm.__init__'   , return_value = None)
    @mock.patch ('BleComm.BleComm.clientSock')
    @mock.patch ('BleComm.BleComm.sock'       , return_value = [0, 0])
    @mock.patch ('BleComm.BleComm.rtos'       , create       = True)
    @mock.patch ('BleComm.BleComm.isRunning'  , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isConnected', return_value = True)
    @mock.patch ('Mpu9250.Mpu9250.isExiting'  , side_effect  = [False, True])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'  , return_value = [100, -100, 100])
    def getImuAngles (self, vMockGetAngles, vIsExistingInBleComm, vIsConnectedInBleComm, 
                         vIsRunningInBleComm, vRtosInBleComm, vSockInBleComm, vClientSockInBleComm,
                         vInitInBleComm, vIsAppExitingInApp, vIsRunningInApp, vIsPausedInApp,
                         vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "getImuAngles")
        serializedImu = b'\x12\x0f\x08d\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18d'
        vClientSockInBleComm.recv.return_value = serializedImu

        self.process.__init__ ()
        vClientSockInBleComm.recv.assert_called      ()
        #vSockInBleComm      .send.assert_called_with (serializedImu)
        self.assertEqual (self.process.settings.imuAnglesMsg.Roll , 100)
        self.assertEqual (self.process.settings.imuAnglesMsg.Pitch, -100)
        self.assertEqual (self.process.settings.imuAnglesMsg.Yaw  , 100)

    def tearDown (self) -> None:
        return super().tearDown ()
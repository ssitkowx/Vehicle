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

    @classmethod    # todo sylsit is this needed?
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.App.isRunning'               , return_value = False)
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , return_value = False)
    @mock.patch ('BleComm.BleComm.isReceiveRunning', return_value = False)
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , return_value = False)
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def setUpClass (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                          vIsConnectedInBleComm, vInitInBleComm, vIsRunningInApp, vSleepInApp):
        LOGI (self.module, "MotorFixture")
        self.process = Process ()

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def stop (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                    vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                    vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "stop")
        serializedImu     = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedStopMsg = b'\n\x02\x10\x01'
        vReciveInBleComm.return_value = serializedStopMsg
        self.process.__init__ ()

        vMotor1       .set.assert_called_with (0)
        vMotor2       .set.assert_called_with (0)
        vSendInBleComm.assert_called_with     (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def moveForwardWithDuty (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                                   vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                                   vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "moveForwardWithDuty")
        serializedImu        = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedForwardMsg = b'\n\x04\x08d\x10\x02'
        vReciveInBleComm.return_value = serializedForwardMsg
        self.process.__init__ ()

        vMotor1       .set.assert_called_with (1)
        vMotor2       .set.assert_called_with (1)
        vSendInBleComm.assert_called_with     (serializedImu)
    
    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def moveBackwardWithDuty (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                                    vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                                    vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "moveBackwardWithDuty")
        serializedImu         = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedBackwardMsg = b'\n\r\x08\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x02'
        vReciveInBleComm.return_value = serializedBackwardMsg
        self.process.__init__ ()

        vMotor1       .set.assert_called_with (-1)
        vMotor2       .set.assert_called_with (-1)
        vSendInBleComm.assert_called_with     (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def turnLeft (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                        vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                        vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "turnLeft")
        serializedImu         = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedTurnLeftMsg = b'\n\x04\x082\x10\x02'
        vReciveInBleComm.return_value = serializedTurnLeftMsg

        self.process.__init__ ()
        vMotor1       .set.assert_any_call (0)
        vMotor1       .set.assert_any_call (0.5)
        vMotor2       .set.assert_any_call (0.5)
        vSendInBleComm.assert_called_with  (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [10, -70, 60])
    def turnRight (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                         vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                         vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "turnRight")
        serializedImu          = b'\x12\x0f\x08\n\x10\xba\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18<'
        serializedTurnRightMsg = b'\n\r\x08\xce\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x03'
        vReciveInBleComm.return_value = serializedTurnRightMsg

        self.process.__init__ ()
        vMotor1       .set.assert_any_call (-0.5)
        vMotor2       .set.assert_any_call (0)
        vMotor2       .set.assert_any_call (-0.5)
        vSendInBleComm.assert_called_with  (serializedImu)

    @mock.patch ('App.time.sleep')
    @mock.patch ('App.motor1'                      , create       = True)
    @mock.patch ('App.motor2'                      , create       = True)
    @mock.patch ('App.App.isRunning'               , side_effect  = [True, False, False])
    @mock.patch ('BleComm.BleComm.__init__'        , return_value = None)
    @mock.patch ('BleComm.BleComm.send')
    @mock.patch ('BleComm.BleComm.receive')
    @mock.patch ('BleComm.BleComm.isConnected'     , return_value = True)
    @mock.patch ('BleComm.BleComm.isSendRunning'   , side_effect  = [True, False])
    @mock.patch ('BleComm.BleComm.isReceiveRunning', side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.isRunning'       , side_effect  = [True, False])
    @mock.patch ('Mpu9250.Mpu9250.getAngles'       , return_value = [100, -100, 100])
    def getImuAngles (self, vMockGetAngles, vIsRunningInMpu9250, vIsReceiveRunningInBleComm, vIsSendRunningInBleComm,
                            vIsConnectedInBleComm, vReciveInBleComm, vSendInBleComm, vInitInBleComm, vIsRunningInApp,
                            vMotor2, vMotor1, vSleepInApp):
        LOGI (self.module, "getImuAngles")
        serializedImu = b'\x12\x0f\x08d\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18d'
        vReciveInBleComm.return_value = serializedImu

        self.process.__init__ ()
        vReciveInBleComm.assert_called      ()
        vSendInBleComm  .assert_called_with (serializedImu)
        self.assertEqual (self.process.settings.imuAnglesMsg.Roll , 100)
        self.assertEqual (self.process.settings.imuAnglesMsg.Pitch, -100)
        self.assertEqual (self.process.settings.imuAnglesMsg.Yaw  , 100)

    def tearDown (self) -> None:
        return super().tearDown ()
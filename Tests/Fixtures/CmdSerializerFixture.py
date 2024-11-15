import unittest
import Cmd_pb2 as CmdProto

from   Logger        import *
from   Settings      import Settings
from   CmdSerializer import CmdSerializer

class CmdSerializerFixture (unittest.TestCase):
    module = __name__
    
    def setUp (self) -> None:
        LOGI (self.module, "CmdSerializerFixture")

        self.settings      = Settings ()
        self.cmdSerializer = CmdSerializer (self.settings)
        return super ().setUp ()
    
    def serializeStop (self):
        LOGI (self.module, 'Serialize stop')

        expectedSerialized                 = b'\n\x02\x10\x01'
        self.settings.vehicleMsg.Duty      = 0
        self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index
        serialized                         = self.cmdSerializer.cmd ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)
    
    def serializeForward (self):
        LOGI (self.module, 'Serialize forward')

        expectedSerialized                 = b'\n\x04\x08d\x10\x01'
        self.settings.vehicleMsg.Duty      = 100
        self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index
        serialized                         = self.cmdSerializer.cmd ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)

    def serializeBackward (self):
        LOGI (self.module, 'Serialize backward')

        expectedSerialized                 = b'\n\r\x08\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01'
        self.settings.vehicleMsg.Duty      = -100
        self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index
        serialized                         = self.cmdSerializer.cmd ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)

    def serializeLeft (self):
        LOGI (self.module, 'Serialize left')

        expectedSerialized                 = b'\n\x04\x082\x10\x02'
        self.settings.vehicleMsg.Duty      = 50
        self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Left'].index
        serialized                         = self.cmdSerializer.cmd ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)

    def serializeRight (self):
        LOGI (self.module, 'Serialize right')

        expectedSerialized                 = b'\n\r\x08\xce\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x03'
        self.settings.vehicleMsg.Duty      = -50
        self.settings.vehicleMsg.Direction = CmdProto.EDirection.DESCRIPTOR.values_by_name['Right'].index
        serialized                         = self.cmdSerializer.cmd ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)
    
    def serializeImu (self):
        LOGI (self.module, 'Serialize imu')

        expectedSerialized               = b'\x12\x0f\x08d\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18d'
        self.settings.imuAnglesMsg.Roll  = 100
        self.settings.imuAnglesMsg.Pitch = -100
        self.settings.imuAnglesMsg.Yaw   = 100
        serialized                       = self.cmdSerializer.imu ()
        print ("Serialized data: ", serialized)
        self.assertEqual (expectedSerialized, serialized)

    def tearDown (self) -> None:
        return super().tearDown ()
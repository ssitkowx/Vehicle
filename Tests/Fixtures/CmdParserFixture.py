import unittest
import Cmd_pb2 as CmdProto

from   Logger    import *
from   Settings  import Settings
from   CmdParser import CmdParser

class CmdParserFixture (unittest.TestCase):
    module = __name__
    
    def setUp (self) -> None:
        LOGI (self.module, "CmdParserFixture")
        self.settings  = Settings ()
        self.cmdParser = CmdParser (self.settings)
        return super ().setUp ()

    def parseForward (self):
        LOGI (self.module, 'Parse forward')
        
        serialized = b'\n\x0b\t\x00\x00\x00\x00\x00\x00\xf0?\x10\x02'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 1)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index)

    def parseBackward (self):
        LOGI (self.module, 'Parse backward')
        
        serialized = b'\n\x0b\t\x00\x00\x00\x00\x00\x00\xf0\xbf\x10\x02'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, -1)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.DESCRIPTOR.values_by_name['Move'].index)

    def parseLeft(self):
        LOGI (self.module, 'Parse left')
        
        serialized = b'\n\x02\x10\x03'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 0)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.DESCRIPTOR.values_by_name['Left'].index)

    def parseRight (self):
        LOGI (self.module, 'Parse right')
        
        serialized = b'\n\x02\x10\x04'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 0)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.DESCRIPTOR.values_by_name['Right'].index)

    def parseImu (self):
        LOGI (self.module, 'Parse imu')
        
        serialized = b'\x12\x0f\x08d\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x18d'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.imuAnglesMsg.Roll , 100)
        self.assertEqual (self.settings.imuAnglesMsg.Pitch, -100)
        self.assertEqual (self.settings.imuAnglesMsg.Yaw  , 100)

    def tearDown (self) -> None:
        return super().tearDown ()
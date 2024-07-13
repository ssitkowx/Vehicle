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
        
        serialized = b'\t\x00\x00\x00\x00\x00\x00\xf0?\x10\x02'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 1)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.Move)

    def parseBackward (self):
        LOGI (self.module, 'Parse backward')
        
        serialized = b'\t\x00\x00\x00\x00\x00\x00\xf0\xbf\x10\x02'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, -1)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.Move)

    def parseLeft(self):
        LOGI (self.module, 'Parse left')
        
        serialized = b'\x10\x03'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 0)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.Left)

    def parseRight (self):
        LOGI (self.module, 'Parse right')
        
        serialized = b'\x10\x04'
        self.cmdParser.parse (serialized)
        self.assertEqual (self.settings.vehicleMsg.Duty, 0)
        self.assertEqual (self.settings.vehicleMsg.Direction, CmdProto.EDirection.Right)

    def tearDown (self) -> None:
        return super().tearDown ()
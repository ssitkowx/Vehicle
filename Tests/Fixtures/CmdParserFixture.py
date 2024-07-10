import unittest
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

    def parse (self):
        LOGI (self.module, 'parse')
        jsonMsg = '{"Duty": 0.1, \
                    "MoveDirection": 1 \
                   }'
        self.cmdParser.parse (jsonMsg)
        self.assertEqual     (self.settings.Duty.data, 0.1)
        self.assertEqual     (self.settings.direction, Settings.EMoveDirection.Backward)

    def tearDown (self) -> None:
        return super().tearDown ()
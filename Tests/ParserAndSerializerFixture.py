import unittest
from   Logger                 import *
from   Settings               import Settings
from   BleParserAndSerializer import BleParserAndSerializer

class ParserAndSerializerFixture (unittest.TestCase):
    module = __name__
    
    def setUp (self) -> None:
        LOGI (self.module, "ParserAndSerializerFixture")
        self.settings               = Settings ()
        self.bleParserAndSerializer = BleParserAndSerializer (self.settings)
        return super ().setUp ()

    def parse (self):
        LOGI (self.module, 'parse')
        jsonMsg = '{"Duty": 0.1, \
                    "MoveDirection": 1 \
                   }'
        self.bleParserAndSerializer.parse (jsonMsg)
        self.assertEqual                  (self.settings.duty, 0.1)
        self.assertEqual                  (self.settings.direction, Settings.EMoveDirection.Backward)
    
    def serialize (self):
        LOGI (self.module, 'serialize')
        expectedJsonMsg = '{"Duty": 0.1, "MoveDirection": 0}'
        self.settings.duty = Settings.Duty = 0.1
        self.settings.direction = Settings.EMoveDirection.Forward
        jsonMsg                 = self.bleParserAndSerializer.serialize ()
        self.assertEqual (jsonMsg, expectedJsonMsg)

    def tearDown (self) -> None:
        return super().tearDown ()
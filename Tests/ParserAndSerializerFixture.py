import unittest
from   Logger                 import *
from   Settings               import Settings
from   BleParserAndSerializer import BleParserAndSerializer

class ParserAndSerializerFixture (unittest.TestCase):
    def setUp (self) -> None:
        LOGI ("ParserAndSerializerFixture")
        self.settings               = Settings ()
        self.bleParserAndSerializer = BleParserAndSerializer (self.settings)
        return super ().setUp ()

    def parse (self):
        LOGI ('parse')
        jsonMsg = '{"MoveDirection": 1}'
        self.bleParserAndSerializer.parse (jsonMsg)
        self.assertEqual                  (self.settings.direction, Settings.EMoveDirection.Backward)
    
    def serialize (self):
        LOGI ('serialize')
        self.settings.direction = Settings.EMoveDirection.Forward
        jsonMsg                 = self.bleParserAndSerializer.serialize ()
        self.assertEqual (jsonMsg, '{"MoveDirection": 0}')

    def tearDown (self) -> None:
        return super().tearDown ()
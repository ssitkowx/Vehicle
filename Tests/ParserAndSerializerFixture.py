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

    def Parse (self):
        LOGI ('Parse')
        jsonMsg = '{"MoveDirection": 1}'
        self.bleParserAndSerializer.parse (jsonMsg)
        self.assertEqual                  (self.settings.direction, Settings.EMoveDirection.Backward)
    
    def Serialize (self):
        LOGI ('Serialize')
        self.settings.direction = Settings.EMoveDirection.Forward
        jsonMsg                 = self.bleParserAndSerializer.serialize ()
        self.assertEqual (jsonMsg, '{"MoveDirection": 0}')

    def tearDown (self) -> None:
        return super().tearDown ()
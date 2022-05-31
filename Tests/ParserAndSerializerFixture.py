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
        jsonMsg = '{"MoveDirection": "EMoveDirection.Backward"}'
        self.bleParserAndSerializer.parse (jsonMsg)
        self.assertEqual                  (self.settings.direction, "EMoveDirection.Backward")
        LOGI                              (self.settings.direction)
        LOGI                              ('\n')
    
    def Serialize (self):
        LOGI ('Serialize')
        self.settings.direction = "EMoveDirection.Forward"
        jsonMsg                 = self.bleParserAndSerializer.serialize ()
        self.assertEqual (jsonMsg, '{"MoveDirection": "EMoveDirection.Forward"}')
        LOGI             (jsonMsg)
        LOGI             ('\n')

    def tearDown (self) -> None:
        return super().tearDown ()
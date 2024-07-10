import unittest
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
    
    def serialize (self):
        LOGI (self.module, 'serialize')
        expectedJsonMsg = '{"Duty": 0.1, "MoveDirection": 0}'
        self.settings.Duty.data = Settings.Duty.data = 0.1
        self.settings.direction = Settings.EMoveDirection.Forward
        jsonMsg                 = self.cmdSerializer.serialize ()
        self.assertEqual (jsonMsg, expectedJsonMsg)

    def tearDown (self) -> None:
        return super().tearDown ()
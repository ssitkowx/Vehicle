import unittest

from MotorFixture               import MotorFixture
from ParserAndSerializerFixture import ParserAndSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    testSuit.addTest (ParserAndSerializerFixture ('Parse'))
    testSuit.addTest (ParserAndSerializerFixture ('Serialize'))
    testSuit.addTest (MotorFixture               ('MoveLeftUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('MoveRightUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('MoveForwardUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('MoveBackwardUntilMaxSpeedLimit'))
    return testSuit

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run (testSuit())
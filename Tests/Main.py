import unittest
from   MotorFixture               import MotorFixture
from   ParserAndSerializerFixture import ParserAndSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    testSuit.addTest (ParserAndSerializerFixture ('parse'))
    testSuit.addTest (ParserAndSerializerFixture ('serialize'))
    testSuit.addTest (MotorFixture               ('moveLeftUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('moveRightUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('moveForwardUntilMaxSpeedLimit'))
    testSuit.addTest (MotorFixture               ('moveBackwardUntilMaxSpeedLimit'))
    return testSuit

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run (testSuit())
import Paths
import unittest
from   LoggerHw                   import *
from   MotorFixture               import MotorFixture
from   ParserAndSerializerFixture import ParserAndSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    testSuit.addTest (ParserAndSerializerFixture ('parse'))
    testSuit.addTest (ParserAndSerializerFixture ('serialize'))
    testSuit.addTest (MotorFixture               ('moveForwardWithDuty'))
    testSuit.addTest (MotorFixture               ('moveBackwardWithDuty'))
    testSuit.addTest (MotorFixture               ('turnLeft'))
    testSuit.addTest (MotorFixture               ('turnRight'))
    return testSuit

if __name__ == "__main__":
    loggerHw = LoggerHw ()
    Logger.setInst (loggerHw)
    runner = unittest.TextTestRunner()
    runner.run (testSuit())
import Paths
import unittest
from   LoggerHw             import *
from   MotorFixture         import MotorFixture
from   CmdParserFixture     import CmdParserFixture
from   CmdSerializerFixture import CmdSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    testSuit.addTest (CmdParserFixture     ('parse'))
    testSuit.addTest (CmdSerializerFixture ('serialize'))
    testSuit.addTest (MotorFixture         ('moveForwardWithDuty'))
    testSuit.addTest (MotorFixture         ('moveBackwardWithDuty'))
    testSuit.addTest (MotorFixture         ('turnLeft'))
    testSuit.addTest (MotorFixture         ('turnRight'))
    return testSuit

if __name__ == "__main__":
    loggerHw = LoggerHw ()
    Logger.setInst (loggerHw)
    runner = unittest.TextTestRunner()
    runner.run (testSuit())
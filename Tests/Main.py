import Paths
import unittest
import subprocess

from   LoggerHw             import *
from   MotorFixture         import MotorFixture
from   CmdParserFixture     import CmdParserFixture
from   CmdSerializerFixture import CmdSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    testSuit.addTest (CmdSerializerFixture ('serializeForward'))
    testSuit.addTest (CmdSerializerFixture ('serializeBackward'))
    testSuit.addTest (CmdSerializerFixture ('serializeLeft'))
    testSuit.addTest (CmdSerializerFixture ('serializeRight'))

    testSuit.addTest (CmdParserFixture     ('parseForward'))
    testSuit.addTest (CmdParserFixture     ('parseBackward'))
    testSuit.addTest (CmdParserFixture     ('parseLeft'))
    testSuit.addTest (CmdParserFixture     ('parseRight'))

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
import Paths
import unittest

from   LoggerHw             import *
from   VehicleFixture       import VehicleFixture
from   CmdParserFixture     import CmdParserFixture
from   CmdSerializerFixture import CmdSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    #testSuit.addTest (CmdSerializerFixture ('serializeForward'))
    #testSuit.addTest (CmdSerializerFixture ('serializeBackward'))
    #testSuit.addTest (CmdSerializerFixture ('serializeLeft'))
    #testSuit.addTest (CmdSerializerFixture ('serializeRight'))
    #testSuit.addTest (CmdSerializerFixture ('serializeImu'))

    #testSuit.addTest (CmdParserFixture     ('parseForward'))
    #testSuit.addTest (CmdParserFixture     ('parseBackward'))
    #testSuit.addTest (CmdParserFixture     ('parseLeft'))
    #testSuit.addTest (CmdParserFixture     ('parseRight'))
    #testSuit.addTest (CmdParserFixture     ('parseImu'))

    testSuit.addTest (VehicleFixture       ('moveForwardWithDuty'))
    #testSuit.addTest (VehicleFixture       ('moveBackwardWithDuty'))
    #testSuit.addTest (VehicleFixture       ('turnLeft'))
    #testSuit.addTest (VehicleFixture       ('turnRight'))
    #testSuit.addTest (VehicleFixture       ('getImuAngles'))
    return testSuit

if __name__ == "__main__":
    loggerHw = LoggerHw ()
    Logger.setInst (loggerHw)
    runner = unittest.TextTestRunner ()
    runner.run (testSuit ())
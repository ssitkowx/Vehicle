import unittest

from MotorFixture               import MotorFixture
from ParserAndSerializerFixture import ParserAndSerializerFixture

def testSuit ():
    testSuit = unittest.TestSuite()
    #testSuit.addTest (ParserAndSerializerFixture ('Parse'))
    #testSuit.addTest (ParserAndSerializerFixture ('Serialize'))
    testSuit.addTest (MotorFixture               ('MoveForward'))
    return testSuit

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run (testSuit())
# WasRun is derived from TestCase
from TestCase import TestCase


class WasRun(TestCase):
    # Constructor
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasSetUp = 1

import random
import os
import unittest

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    def test_add(self):
        a=1
        b=2
        c=a+b
        self.assertEqual(c,3)
class TestCallExe(unittest.TestCase):
    def test_minus(self):
        a=2
        b=1
        c=a-b
        self.assertEqual(c,1)
    def test_callexe(self):
        print "this is a call in unit test"
        os.spawnv(os.P_NOWAIT, 'C:\Python26\python.exe', ('python', 'Out.py'))
if __name__ == '__main__':
    unittest.main()
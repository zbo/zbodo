import unittest


def func():
    return 'a'


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsum(self):
        self.assertEqual(func(), 'a', 'test fail')


if __name__ == '__main__':
    unittest.main()

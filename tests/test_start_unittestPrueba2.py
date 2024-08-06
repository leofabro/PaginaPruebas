import unittest

class TestStart(unittest.TestCase):

    def test_part1(self):
        self.assertTrue("HELLO".isupper())

    def test_part2(self):
        self.assertFalse("hello".isupper())

if __name__ == "__main__":
    unittest.main()

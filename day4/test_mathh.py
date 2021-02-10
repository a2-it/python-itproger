import unittest
import mathh

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathh.add(5,7), 12)
        self.assertEqual(mathh.add(5,3), 8)

if __name__ == '__main__':
    unittest.main()
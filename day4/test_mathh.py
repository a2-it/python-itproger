import unittest
import mathh

class TestMath(unittest.TestCase):

    def test_add(self):
        result = mathh.add(5,7)
        self.assertEqual(result, 12)

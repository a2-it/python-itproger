import unittest
import math

class TestMath(unittest.TestCase):

    def test_add(self):
        result = math.add(5,7)
        self.assertEqual(result, 12)

import pytest
import mathh
@pytest.mark.parametrize('num1, num2, res', [
    (5,5,10),
    ('Hello','World', 'HelloWorld')
    ])
@pytest.mark.add
def test_add(num1, num2, res):
    assert mathh.add(num1, num2) == res

def test_add():
    assert mathh.mult(4,5) == 20

@pytest.mark.add
def test_addStrings():
    res = mathh.add('Hello','World')
    assert type(res) is str
    assert 'Hello' in res

def test_mult():
    res = mathh.mult(5,5)
    assert res == 25


# import unittest
# import mathh
#
# class TestMath(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEqual(mathh.add(5,7), 12)
#         self.assertEqual(mathh.add(5,3), 8)
#
# if __name__ == '__main__':
#     unittest.main()
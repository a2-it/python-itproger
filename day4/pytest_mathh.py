import pytest
import mathh
@pytest.mark.parametrize('num1, num2, res', [
    (5,5,10),
    ('Hello','World', 'HelloWorld')
    ])
@pytest.mark.add
def test_add(num1, num2, res):
    assert mathh.add(num1, num2) == res

@pytest.mark.add
def test_addStrings():
    res = mathh.add('Hello','World')
    assert type(res) is str
    assert 'Hello' in res

def test_mult():
    res = mathh.mult(5,5)
    assert res == 25
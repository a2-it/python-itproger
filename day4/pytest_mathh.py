import pytest
import mathh

def test_add():
    res = mathh.add(5,5)
    assert res == 10

def test_mult():
    res = mathh.mult(5,5)
    assert res == 25
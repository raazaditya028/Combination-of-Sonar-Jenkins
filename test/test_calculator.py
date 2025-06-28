import pytest
from app.calculator import add,subtract,multiply,divide

def test_add():
    assert add(2,3)==5

def test_subtract():
    assert subtract(10,8)==2

def test_multiply():
    assert multiply(3,9)==27

def test_divide():
    assert divide(200,100)==2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)


from ops import *
import pytest

def test_add_success():
    assert add(2, 2) == 4
    
def test_sub_success():
    assert sub(2, 2) == 0

def test_mul_success():
    assert mul(2, 2) == 4

def test_mul_success_string():
    assert mul('2', 2) == "22"

# def test_div_success():
#     assert div(2, 2) == 1

# Failure scenarios

def test_add_failure():
    with pytest.raises(TypeError):
        assert add('2', 2)
    
def test_sub_failure():
    with pytest.raises(TypeError):
        assert sub('2', 2)

def test_mul_failure():
    with pytest.raises(TypeError):
        assert mul('2', '2')

# def test_div_failure():
#     with pytest.raises(TypeError):
#         assert div('2', 2)

# def test_div_zero():
#     with pytest.raises(ZeroDivisionError):
#         assert div(2, 0)
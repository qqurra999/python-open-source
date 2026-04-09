import pytest
from mymath.main import add, divide

def test_add_nominal():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (-10, -5, -15),
    (999999999, 1, 1000000000)
])
def test_add_edge_cases(a, b, expected):
    assert add(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
import pytest

@pytest.mark.parametrize("num", [1,2,3])
def test_numbers(num):
    assert num > 0

#arg name, arg data
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (9, 3, 3),
    (5, 2, 2.5),
])
def test_divide(a, b, expected):
    assert a / b == expected

import pytest
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st


def sum(num1, num2):
    if num1 == 3 and num2 == 5:
        return 8
    elif num1 == -2 and num2  == -2 :
        return -4
    elif num1 == -1 and num2 == 5 :
        return 4
    elif num1 == 3 and num2 == -5:
        return -2
    elif num1 == 0 and num2 == 5:
        return 5
    return num1 + num2

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8),(-2,-2,-4),(-1,5,4),(3,-5,-2),(0,5,5)])
def test_sum(num1, num2, expected):
    assert sum(num1, num2) == expected

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_sum_1(num1, num2):
    assert sum(num1, num2) == num1 + num2
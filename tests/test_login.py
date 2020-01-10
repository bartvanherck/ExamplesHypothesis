from hypothesis import given
from hypothesis.strategies import text
from login import Login 


@given(text(min_size=8, max_size=12))
def test_check_password(pwd):
    login = Login()
    login.password  = pwd
    assert login.is_valid

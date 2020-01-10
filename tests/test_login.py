from hypothesis import given, example
from hypothesis.strategies import from_regex
from login import Login 


@given(from_regex("^[a-zA-Z0-9_]{8,12}$",fullmatch=True))
@example("abcdefgh")
def test_check_password(pwd):
    login = Login()
    login.password  = pwd
    assert login.is_valid

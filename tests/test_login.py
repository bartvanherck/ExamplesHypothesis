from login import Login 


def test_check_min_minus_1():
    login = Login()
    login.password = "1234567"
    assert login.is_valid == False

def test_check_min():
    login = Login()
    login.password = "12345678"
    assert login.is_valid

def test_check_min_plus_one():
    login = Login()
    login.password = "12345679"
    assert login.is_valid

def test_check_max_minus_1():
    login = Login()
    login.password = "12345678901"
    assert login.is_valid

def test_check_max():
    login = Login()
    login.password = "123456789012"
    assert login.is_valid

def test_check_max_plus_one():
    login = Login()
    login.password = "1234567890123"
    assert login.is_valid == False

def test_weird_chars():
    login = Login()
    login.password = "123456-89012"
    assert login.is_valid == False

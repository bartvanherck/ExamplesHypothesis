from login import Login 

def test_check_password():
    login = Login()
    login.password  = "abcd"
    assert login.is_valid

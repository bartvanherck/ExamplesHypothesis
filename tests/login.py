class Validator(object):
    def check(self, input):
        if len(input) < 8:
            return False
        elif len(input) > 12:
            return False
        return True


class Login():
    def __init__(self):
        self.__pwd = None
    
    @property
    def password(self):
        return self.__pwd

    @password.setter
    def password(self, value):
        self.__pwd = value

    @property
    def is_valid(self):
        return Validator().check(self.__pwd)

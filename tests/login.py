class Validator(object):
    pass


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
        return True

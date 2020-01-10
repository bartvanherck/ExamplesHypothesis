import string


class Validator(object):
    def check(self, input):
        if len(input) < 8:
            return False
        elif len(input) > 12:
            return False
        return not self.has_invalid_chars(input)

    def has_invalid_chars(self, input):
        invalid = set(string.punctuation.replace("_",""))
        if any(char in invalid for char in input):
            return True
        return False


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

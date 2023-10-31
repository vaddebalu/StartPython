class NumberLimitException(Exception):
    def __int__(self):
        Exception.__int__(self)
    def respond(self):
        raise ArithmeticError("Number limit exceeded")
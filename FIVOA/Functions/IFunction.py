from Point import *

class IFunction(object):
    def __init__(self):
        self.__counter = 0

    def increment_numer_of_calls(self):
        self.__counter += 1

    def get_number_of_calls(self):
        return self.__counter

    def value_at(self, point):
        raise NotImplementedError

    def gradient_at(self, point):
        raise NotImplementedError

    def hessian_at(self, point):
        raise NotImplementedError
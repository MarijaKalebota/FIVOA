from Point import *

class IFunction(object):

    def value_at(self, point):
        raise NotImplementedError

    def gradient_at(self, point):
        raise NotImplementedError

    def hessian_at(self, point):
        raise NotImplementedError

    def get_number_of_calls(self):
        raise NotImplementedError
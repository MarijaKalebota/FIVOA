from IFunction import *

class F4TwoLocalOptima(IFunction):

    def value_at(self, point):
        self.increment_number_of_calls()
        return point.get_value_at_dimension(0) ** 4 - point.get_value_at_dimension(0) ** 2 + point.get_value_at_dimension(0) / 10

    def gradient_at(self, point):
        return 4 * point.get_value_at_dimension(0) ** 3 - 2 * point.get_value_at_dimension(0) + 0.1

    def hessian_at(self, point):
        raise NotImplementedError
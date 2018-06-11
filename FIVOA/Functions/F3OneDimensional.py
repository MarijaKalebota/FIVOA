from IFunction import *

class F3OneDimensional(IFunction):

    def value_at(self, point):
        #self.increment_number_of_calls()
        return (point.get_value_at_dimension(0) - 3) ** 2

    def gradient_at(self, point):
        return 2 * (point.get_value_at_dimension(0) - 3)

    def hessian_at(self, point):
        raise NotImplementedError
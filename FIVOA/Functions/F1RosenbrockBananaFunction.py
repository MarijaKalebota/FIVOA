from IFunction import *

class F1RosenbrockBananaFunction(IFunction):

    def value_at(self, point):
        #self.increment_number_of_calls()
        return 100 * (point.get_value_at_dimension(1) - point.get_value_at_dimension(0)**2)**2 + (1 - point.get_value_at_dimension(0))**2

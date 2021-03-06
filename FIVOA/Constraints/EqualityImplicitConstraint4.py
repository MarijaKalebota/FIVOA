from IEqualityImplicitConstraint import *

class EqualityImplicitConstraint4(IEqualityImplicitConstraint):
    def is_satisfied(self, point):
        #if (point.get_value_at_dimension(1) - point.get_value_at_dimension(0) + 50 == 0):
        #if (point.get_value_at_dimension(1) - point.get_value_at_dimension(0) + 5 == 0):
        if (point.get_value_at_dimension(0) - point.get_value_at_dimension(1) == 0):
            return True
        else:
            return False

    def value_at(self, point):
        #return point.get_value_at_dimension(1) - point.get_value_at_dimension(0) + 50
        #return point.get_value_at_dimension(1) - point.get_value_at_dimension(0) + 5
        return point.get_value_at_dimension(0) - point.get_value_at_dimension(1)

    def get_gradient(self):
        raise NotImplementedError
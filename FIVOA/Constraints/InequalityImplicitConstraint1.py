from IInequalityImplicitConstraint import *

class InequalityImplicitConstraint1(IInequalityImplicitConstraint):
    def is_satisfied(self, point):
        if(point.get_value_at_dimension(1) - point.get_value_at_dimension(0) >= 0):
            return True
        else:
            return False

    def value_at(self, point):
        return point.get_value_at_dimension(1) - point.get_value_at_dimension(0)

    def get_gradient(self):
        raise NotImplementedError
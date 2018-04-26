from IInequalityImplicitConstraint import *

class InequalityImplicitConstraint1(IInequalityImplicitConstraint):
    def is_satisfied(self, point):
        if(point.getElement(0,1) - point.getElement(0,0) >= 0):
            return True
        else:
            return False

    def value_at(self, point):
        return point.getElement(0,1) - point.getElement(0,0)

    def get_gradient(self):
        raise NotImplementedError
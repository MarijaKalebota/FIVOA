from IInequalityImplicitConstraint import *

class InequalityImplicitConstraint2(IInequalityImplicitConstraint):
    def is_satisfied(self, point):
        if(2 - point.getElement(0,0) >= 0):
            return True
        else:
            return False

    def value_at(self, point):
        return 2 - point.getElement(0,0)

    def get_gradient(self):
        raise NotImplementedError
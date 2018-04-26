from IImplicitConstraint import *

class IInequalityImplicitConstraint(IImplicitConstraint):

    def is_satisfied(self, point):
        raise NotImplementedError

    def value_at(self, point):
        raise NotImplementedError

    def get_gradient(self):
        raise NotImplementedError
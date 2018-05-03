class ExplicitConstraintForOneDimension(object):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_satisfied(self, value):
        if(value > self.upper_bound or value < self.lower_bound):
            return False
        else:
            return True

    def value_at(self, point):
        raise NotImplementedError
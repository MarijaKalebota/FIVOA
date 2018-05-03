class ExplicitConstraintForOneDimension(object):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def get_lower_bound(self):
        return self.lower_bound

    def get_upper_bound(self):
        return self.upper_bound

    def is_satisfied(self, value):
        if(value > self.get_upper_bound() or value < self.get_lower_bound()):
            return False
        else:
            return True

    def value_at(self, point):
        raise NotImplementedError
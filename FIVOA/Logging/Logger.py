class Logger(object):
    def __init__(self, function):
        self.function = function
        self.iterations = []
        self.explicit_constraints = []
        self.equality_implicit_constraints = []
        self.inequality_implicit_constraints = []

    def add_iteration(self, iteration):
        self.iterations.append(iteration)

    def get_iterations(self):
        return self.iterations

    def get_iteration(self, index):
        if(len(self.iterations) >= index):
            return "Index out of range"
        else:
            return self.iterations[index]

    def get_function(self):
        return self.function

    def add_explicit_constraint(self, constraint):
        self.explicit_constraints.append(constraint)

    def get_explicit_constraints(self):
        return self.explicit_constraints

    def get_explicit_constraint(self, index):
        return self.explicit_constraints[index]

    def set_explicit_constraints(self, constraints):
        self.explicit_constraints = constraints

    def add_inequality_implicit_constraint(self, constraint):
        self.inequality_implicit_constraints.append(constraint)

    def get_inequality_implicit_constraints(self):
        return self.inequality_implicit_constraints

    def get_inequality_implicit_constraint(self, index):
        return self.inequality_implicit_constraints[index]

    def set_inequality_implicit_constraints(self, constraints):
        self.inequality_implicit_constraints = constraints

    def add_equality_implicit_constraint(self, constraint):
        self.equality_implicit_constraints.append(constraint)

    def get_equality_implicit_constraints(self):
        return self.equality_implicit_constraints

    def get_equality_implicit_constraint(self, index):
        return self.equality_implicit_constraints[index]

    def set_equality_implicit_constraints(self, constraints):
        self.equality_implicit_constraints = constraints
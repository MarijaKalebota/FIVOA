class Logger(object):
    def __init__(self, function):
        self.function = function
        self.iterations = []
        self.explicit_constraints = []
        self.implicit_constraints = []

    def add_iteration(self, iteration):
        self.iterations.append(iteration)

    def get_iteration(self, index):
        if(index >= len(self.iterations)):
            raise IndexError("That index is bigger than the maximum number of iterations")
        else:
            return self.iterations[index]

    def get_number_of_iterations(self):
        return len(self.iterations)

    def get_function(self):
        return self.function

    def add_explicit_constraint(self, constraint):
        self.explicit_constraints.append(constraint)

    def get_explicit_constraint(self, index):
        return self.explicit_constraints[index]

    def get_explicit_constraints(self,):
        return self.explicit_constraints

    def get_number_of_explicit_constraints(self):
        return len(self.explicit_constraints)

    def set_explicit_constraints(self, constraints):
        self.explicit_constraints = constraints

    def add_implicit_constraint(self, constraint):
        self.implicit_constraints.append(constraint)

    def get_implicit_constraint(self, index):
        return self.inequality_implicit_constraints[index]

    def get_implicit_constraints(self):
        return self.inequality_implicit_constraints

    def get_number_of_implicit_constraints(self):
        return len(self.implicit_constraints)

    def set_implicit_constraints(self, constraints):
        self.inequality_implicit_constraints = constraints
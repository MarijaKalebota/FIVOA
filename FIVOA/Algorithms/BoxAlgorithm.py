import random

from IAlgorithm import *
from Point import *
from Logging.Logger import *
from Logging.Iteration import *

class BoxAlgorithm(IAlgorithm):

    #def __init__(self, function, lower_bounds, upper_bounds, implicit_constraints, epsilon, alpha, print_me):
    #def __init__(self, function, explicit_constraints, implicit_constraints, epsilon, alpha, print_me):
    def __init__(self, function, explicit_constraints, implicit_constraints, epsilon, alpha):
        self.function = function
        #self.lower_bounds = lower_bounds
        #self.upper_bounds = upper_bounds
        self.explicit_constraints = explicit_constraints
        self.implicit_constraints = implicit_constraints
        self.epsilon = epsilon
        self.alpha = alpha
        #self.print_me = print_me

    @staticmethod
    def reflect(xc, xh, alpha):
        return xc.multiply_by_scalar(1 + alpha) - xh.multiply_by_scalar(alpha)

    def get_logger(self):
        return self.logger


    def run(self, initial_point):
        additional_data = {}

        n = initial_point.get_number_of_dimensions()

        for i in range(n):
            #if(initial_point.getElement(0, i) < self.lower_bounds[i] or initial_point.getElement(0, i) > self.upper_bounds[i]):
            if not self.explicit_constraints[i].is_satisfied(initial_point.get_value_at_dimension(i)):
                print "The given initial_point is not within the explicit constraints."
                return

        centroid = initial_point.copy()

        accepted_points = []

        accepted_points.append(initial_point)

        for t in range(2*n):
            elements = []
            for i in range(n):
                elements.append(0)
                R = random.uniform(0, 1)
                elements[i] = self.explicit_constraints[i].get_lower_bound() + R * (self.explicit_constraints[i].get_upper_bound() - self.explicit_constraints[i].get_lower_bound())

            new_point = Point(elements)
            for j in range(len(self.implicit_constraints)):
                while (not self.implicit_constraints[j].is_satisfied(new_point)):
                    new_point = (new_point + centroid).multiply_by_scalar(0.5)

            accepted_points.append(new_point)

            #calculate new centroid (with new accepted initial_point)
            sum_elements = []
            for i in range(n):
                sum_elements.append(0)

            sum = Point(sum_elements)
            for i in range(len(accepted_points)):
                sum = sum + accepted_points[i]
            #centroid = sum/(simplex.length - 2);
            centroid = sum.multiply_by_scalar(1.0/len(accepted_points))

        keepGoing = True
        iteration_number = 1
        logger = Logger(self.function)
        logger.set_implicit_constraints(self.implicit_constraints)
        while(keepGoing):
            MIN = float('-inf')
            max = MIN
            value_at_xh = MIN
            value_at_xh2 = MIN
            xh_index = 0
            xh2_index = 0
            for i in range(len(accepted_points)):
                if(self.function.value_at(accepted_points[i]) > self.function.value_at(accepted_points[xh_index])):
                    xh2_index = xh_index
                    xh_index = i

            #calculate centroid without xh
            sum_elements = []
            for i in range(n):
                sum_elements.append(0)
            sum = Point(sum_elements)
            #for (int i = 0; i < accepted_points.size(); i++) {
            for i in range(len(accepted_points)):
                if( i == xh_index):
                    pass
                else:
                    sum = sum + accepted_points[i]

            #centroid = Matrix.scalarMultiply(sum, (1.0/(len(accepted_points) - 1)))
            centroid = sum.multiply_by_scalar((1.0/(len(accepted_points) - 1)))
            xr = self.reflect(centroid, accepted_points[xh_index], self.alpha)
            for i in range(n):
                #if(xr.getElement(0,i) < self.lower_bounds[i]):
                lower_bound = self.explicit_constraints[i].get_lower_bound()
                upper_bound = self.explicit_constraints[i].get_upper_bound()
                if (xr.get_value_at_dimension(i) < lower_bound):
                    xr.set_value_at_dimension(i, lower_bound)
                elif(xr.get_value_at_dimension(i) > upper_bound):
                    xr.set_value_at_dimension(i, upper_bound)

            for i in range(len(self.implicit_constraints)):
                while (not self.implicit_constraints[i].is_satisfied(xr)):
                    xr = (xr + centroid).multiply_by_scalar(0.5)

            if(self.function.value_at(xr) > self.function.value_at(accepted_points[xh2_index])):
                xr = (xr + centroid).multiply_by_scalar(0.5)

            accepted_points[xh_index] = xr

            keepGoing = False
            for i in range(len(accepted_points)):
                if(abs(self.function.value_at(accepted_points[i]) - self.function.value_at(centroid)) > self.epsilon):
                    keepGoing = True


            #TODO check if this is the correct place to log the additional_data points

            xh_description = "xh - The initial_point in which the function value is highest"
            xr_description = "xr - Reflected initial_point"
            xc_description = "xc - Centroid"

            xh_tuple = (accepted_points[xh_index], xh_description)
            xr_tuple = (xr, xr_description)
            xc_tuple = (centroid, xc_description)

            additional_data["xh"] = xh_tuple
            additional_data["xr"] = xr_tuple
            additional_data["xc"] = xc_tuple

            currentIteration = Iteration(iteration_number, self.function.value_at(centroid), centroid, additional_data, self.function.get_number_of_calls())
            logger.add_iteration(currentIteration)

            iteration_number = iteration_number + 1

        return centroid, logger
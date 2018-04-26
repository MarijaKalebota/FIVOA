from IAlgorithm import *
from Point import *
from Logging.Logger import *
from Logging.Iteration import *

class HookeJeeves(IAlgorithm):

    def __init__(self, f, step, factor, epsilon, print_me):
        self.f = f
        self.step = step
        self.factor = factor
        self.epsilon = epsilon
        self.print_me = print_me
        self.logger = Logger(self.f)

    def get_logger(self):
        return self.logger

    #@staticmethod
    def run(self, initial_point):
        #f = open('HookeJeevesOutput.txt', 'w')
        output_string = ""
        xb = initial_point.copy()
        xp = initial_point.copy()
        xn = initial_point.copy()
        iteration_number = 0

        while (self.step > self.epsilon):
            additional_data = {}
            #find xn
            if (self.print_me):
                print "Iteration: " + str(iteration_number + 1)
            for i in range(xn.get_number_of_dimensions()):
                plus = xn.copy()
                #plus.getElements()[0,i] = plus.getElements()[0,i] + self.step
                plus.set_value_at_dimension(plus.get_value_at_dimension(i) + self.step)
                minus = xn.copy()
                #minus.getElements()[0,i] = minus.getElements()[0,i] - self.step
                minus.set_value_at_dimension(minus.get_value_at_dimension(i) - self.step)

                current_minimum = xn
                #test = self.f.valueAt(plus)
                #test2 = self.f.valueAt(minus)
                if (self.f.valueAt(plus) < self.f.valueAt(current_minimum)):
                    current_minimum = plus
                if (self.f.valueAt(minus) < self.f.valueAt(current_minimum)):
                    current_minimum = minus
                xn = current_minimum

            if (self.print_me):
                #TODO printing
                print "xb = "
                #Matrix.printMatrix(xb)
                print "\txp = "
                #Matrix.printMatrix(xp)
                print "\txn = "
                #Matrix.printMatrix(xn)
                print "Step = " + str(self.step)

            xb_description = "xb - Bazna tocka algoritma Hooke-Jeeves"
            xp_description = "xp - Tocka pretrazivanja algoritma Hooke-Jeeves u trenutnoj iteraciji. xp' = 2*xn + xb"
            xn_description = "xn - Nova tocka algoritma Hooke-Jeeves, izracunata (dobivena pretrazivanjem) u trenutnoj iteraciji, Ona u sljedecoj iteraciji postaje bazna tocka."

            xb_tuple = (xb, xb_description)
            xp_tuple = (xp, xp_description)
            xn_tuple = (xn, xn_description)

            additional_data["xb"] = xb_tuple
            additional_data["xp"] = xp_tuple
            additional_data["xn"] = xn_tuple

            currentIteration = Iteration(iteration_number, self.f.valueAt(xn), xn, additional_data)
            self.logger.addIteration(currentIteration)

            if (self.f.valueAt(xn) < self.f.valueAt(xb)):
                xp = xn.multiply_by_scalar(2) - xb

                xb = xn.copy()
                xn = xp.copy()
            else:
                self.step = self.step * self.factor
                if (self.print_me):
                    print "Changing step to " + str(self.step)
                xp = xb.copy()
                xn = xp.copy

            iteration_number = iteration_number + 1
            output_string = output_string + str(xn.get_value_at_dimension(0))
            for i in range(1, xn.get_number_of_dimensions()):
                output_string = output_string + " " + str(xn.get_value_at_dimension(i))
            output_string = output_string + "\n"
        print "Final solution of Hooke-Jeeves search for initial point " + str(initial_point.get_value_at_dimension(0)) + " is " + str(xb.getElements())
        output = open('HookeJeevesOutput.txt', 'w')
        output.write(output_string)
        return xb
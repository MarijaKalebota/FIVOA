from Point import *

class Iteration():
    def __init__(self, iteration_number, function_value_in_current_solution, current_solution_point, additional_data, number_of_function_calls):
        self.iteration_number = iteration_number
        self.current_solution_point = current_solution_point
        self.function_value_in_current_solution = function_value_in_current_solution
        self.number_of_function_calls = number_of_function_calls
        self.additional_data = additional_data

    def get_iteration_number(self):
        return self.iteration_number

    def get_function_value(self):
        return self.function_value

    def get_current_solution(self):
        return self.current_solution_point

    def get_additional_data(self):
        return self.additional_data

    def get_number_of_function_calls(self):
        return self.number_of_function_calls
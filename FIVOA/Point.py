import numpy as np

class Point:
    def __init__(self, number_of_dimensions, elements):
        self.number_of_dimensions = number_of_dimensions
        self.elements = elements

    def get_value_at_dimension(self, index):
        return self.elements[index]

    def set_value_at_dimension(self, index, new_value):
        self.elements[index] = new_value

    def get_number_of_dimensions(self):
        return self.number_of_dimensions

    def copy(self):
        new_elements = self.get_elements()
        number_of_dimensions = self.get_number_of_dimensions()
        new_point = Point(number_of_dimensions, new_elements)
        return new_point

    def multiply_by_scalar(self, scalar):
        new_point = self.copy()
        number_of_dimensions_of_point = new_point.get_number_of_dimensions()

        for i in range(len(number_of_dimensions_of_point)):
            new_point.set_value_at_dimension(i, new_point.get_value_at_dimension(i) * scalar)

        return new_point
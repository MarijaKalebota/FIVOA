import numpy as np

class Vector:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point
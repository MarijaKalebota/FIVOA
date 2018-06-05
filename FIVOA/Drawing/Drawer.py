import numpy as np
import matplotlib.pyplot as plt
from Point import *
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
import numbers

class Drawer:
    def __init__(self, logger):
        self.logger = logger
        self.points = []
        self.constraints = []

    def add_function(self, function):
        self.function = function

    def add_point(self, point):
        self.points.append(point)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def draw_2D_gaph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
        plt.clf()
        plt.close('all')
        # TODO need this?
        #plt.figure(iteration)
        plt.axis([min_X1, max_X1, min_X2, max_X2])
        ax = plt.gca()
        ax.set_autoscale_on(False)

        X = np.linspace(min_X1, max_X1, num=number_of_samples_of_domain)
        Y = [self.function.valueAt(x) for x in X]
        plt.plot(X, Y, 'b')

        # TODO constraints

        #plt.plot(x_value_of_current_optimum, y_value_of_current_optimum, 'ro')
        for point in self.points:
            plt.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1), 'ro')
        plt.show()

    def draw_contour_graph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
        plt.clf()
        plt.close('all')
        #TODO need this?
        #plt.figure(iteration)
        plt.axis([min_X1, max_X1, min_X2, max_X2])
        ax = plt.gca()
        ax.set_autoscale_on(False)

        X1_linspace = np.linspace(min_X1, max_X1, num=number_of_samples_of_domain)
        X2_linspace = np.linspace(min_X2, max_X2, num=number_of_samples_of_domain)

        X1, X2 = np.meshgrid(X1_linspace, X2_linspace)

        def create_Z(x, y, function):
            new_point = Point(2, [x, y])
            return function.valueAt(new_point)

        Z = create_Z(X1, X2, self.function)

        plt.contourf(X1, X2, Z, 20, cmap='RdGy')
        plt.colorbar();

        #TODO constraints

        #plt.plot(xRjesenja[iteration], yRjesenja[iteration], 'go')
        for point in self.points:
            plt.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1), 'go')
        plt.show()

    def draw_3D_graph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain, cmap):
        plt.clf()
        plt.close('all')
        #plt.figure(iteration_number)
        ax = plt.axes(projection='3d')

        # region Create fixed arrays for graph
        X1_linspace = np.linspace(min_X1, max_X1, number_of_samples_of_domain)
        X2_linspace = np.linspace(min_X2, max_X2, number_of_samples_of_domain)

        X1_for_graph, X2_for_graph = np.meshgrid(X1_linspace, X2_linspace)
        Z_for_graph = []
        for x2 in X2_linspace:
            Z = []
            for x1 in X1_linspace:
                #elements = np.array([[x1, x2]])
                #matrix_x1_x2 = Matrix(1, 2, elements)
                new_point = Point(2, [x1, x2])
                Z.append(self.function.valueAt(new_point))
            Z_for_graph.append(Z)
        # endregion

        # Plot fixed graph
        ax.contour3D(X1_for_graph, X2_for_graph, Z_for_graph, 50, cmap=cmap)
        # plt.plot([-1.9], [2.0], 'b')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')

        #TODO constraints

        # Plot all points from internal list
        for point in self.points:
            ax.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1),
                    point.get_value_at_dimension(2),
                    markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=1)
        plt.show()


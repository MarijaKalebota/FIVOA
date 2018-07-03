import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#from Point import *
#import Point
#from FIVOA.Point import *
import os, sys



parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
import Constraints
from Point import *
#from Point import Point
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
import numbers
#from Constraints import *


import inspect


class Drawer:
    '''
    def __init__(self, logger):
        self.logger = logger
        self.points = []
        self.constraints = []
        '''

    #def __init__(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
    def __init__(self):
        self.points = []
        self.constraints = []
        self.number_of_samples_of_domain = 150
        self.ranges_of_variables = [ [-10, 10],
                                     [-15, 15]
                                     ]
        self.cmap = 'Accent'
        self.constraints_colormap = 'autumn'
        self.figure_number = 0
        self.twoD_graph_function_colour = 'b'
        self.twoD_graph_point_style = 'go'

    def add_function(self, function):
        self.function = function

    def add_point(self, point):
        self.points.append(point)

    def clear_points(self):
        self.points = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def set_ranges_of_variables(self, ranges):
        self.ranges_of_variables = ranges

    def get_range_of_variable(self, index_of_variable):
        return self.ranges_of_variables[index_of_variable]

    def set_number_of_samples_of_domain(self, number_of_samples_of_domain):
        #TODO maybe make this an array - to be able to sample different variables differently?
        self.number_of_samples_of_domain = number_of_samples_of_domain

    def get_number_of_samples_of_domain(self):
        return self.number_of_samples_of_domain

    def set_cmap(self, cmap):
        self.cmap = cmap

    def set_constraints_cmap(self, cmap):
        self.constraints_colormap = cmap

    def set_2D_graph_function_colour(self, colour):
        self.twoD_graph_function_colour = colour

    def set_2D_graph_point_style(self, point_style):
        self.twoD_graph_point_style = point_style

    def set_figure_number(self, fig_num):
        self.figure_number = fig_num

    def is_within_margin(self, value, margin):
        if abs(value) <= margin:
            return True
        else:
            return False

    def remove_constrained_area_from_main_graph(self, Z_for_graph, Z_of_constraint):
        for i in range(len(Z_for_graph)):
            for j in range(len(Z_for_graph[i])):
                if np.isnan(Z_of_constraint[i][j]):
                    # Z_for_graph should stay as it is
                    pass
                else:
                    Z_for_graph[i][j] = np.nan
        return Z_for_graph

    def create_graph_data_for_explicit_constraint(self, X1_for_graph_before_meshgrid, X2_for_graph_before_meshgrid, constraint, this_is_for_X1):
        Z_of_constraint = []

        for x2 in X2_for_graph_before_meshgrid:
            Z = []
            for x1 in X1_for_graph_before_meshgrid:
                if (this_is_for_X1):
                    if (constraint.is_satisfied(x1) is True):
                        Z.append(np.nan)
                    else:
                        point = Point([x1, x2])
                        Z.append(self.function.value_at(point))
                else:
                    if (constraint.is_satisfied(x2) is True):
                        Z.append(np.nan)
                    else:
                        point = Point([x1, x2])
                        Z.append(self.function.value_at(point))
            Z_of_constraint.append(Z)
        return Z_of_constraint

    def create_graph_data_for_equality_implicit_constraint(self, X1_for_graph_before_meshgrid, X2_for_graph_before_meshgrid, constraint):
        Z_of_constraint = []
        for x2 in X2_for_graph_before_meshgrid:
            Z = []
            for x1 in X1_for_graph_before_meshgrid:
                point = Point([x1, x2])
                distance = constraint.value_at(point)
                if (self.is_within_margin(distance, 5)):
                    # Z.append(distance)
                    Z.append(self.function.value_at(point))
                else:
                    Z.append(np.nan)
            Z_of_constraint.append(Z)
        return Z_of_constraint

    def create_graph_data_for_inequality_implicit_constraint(self, X1_for_graph_before_meshgrid, X2_for_graph_before_meshgrid, constraint):
        Z_of_constraint = []
        for x2 in X2_for_graph_before_meshgrid:
            Z = []
            for x1 in X1_for_graph_before_meshgrid:
                point = Point([x1, x2])
                if (constraint.is_satisfied(point) is True):
                    Z.append(np.nan)
                else:
                    # Z.append(constraint.value_at(matrix_x1_x2))
                    Z.append(self.function.value_at(point))
            Z_of_constraint.append(Z)
        return Z_of_constraint

    #def draw_2D_graph(self, min_X, max_X, min_Y, max_Y, number_of_samples_of_domain):
    def draw_2D_graph(self):
        plt.clf()
        plt.close('all')
        # TODO need this?
        #plt.figure(iteration)
        min_X = self.ranges_of_variables[0][0]
        max_X = self.ranges_of_variables[0][1]
        min_Y = self.ranges_of_variables[1][0]
        max_Y = self.ranges_of_variables[1][1]
        number_of_samples_of_domain = self.number_of_samples_of_domain

        plt.axis([min_X, max_X, min_Y, max_Y])
        ax = plt.gca()
        ax.set_autoscale_on(False)
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        X = np.linspace(min_X, max_X, num=number_of_samples_of_domain)
        X_points = []
        for x in X:
            new_point = Point([x])
            X_points.append(new_point)
        #Y = [self.function.value_at(x) for x in X]
        #Y = [self.function.value_at(x) for x in X_points]
        Y = [self.function.value_at(Point([x])) for x in X]
        plt.plot(X, Y, self.twoD_graph_function_colour)

        # not drawing 2D constraints in this version

        #plt.plot(x_value_of_current_optimum, y_value_of_current_optimum, 'ro')
        for point in self.points:
            plt.plot(point.get_value_at_dimension(0), self.function.value_at(point), self.twoD_graph_point_style)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        #plt.title('Title')
        plt.show()

    #def draw_contour_graph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
    def draw_contour_graph(self):
        plt.clf()
        plt.close('all')
        #TODO need this?
        #plt.figure(iteration)
        cmap = self.cmap
        constraints_cmap = self.constraints_colormap
        min_X1 = self.ranges_of_variables[0][0]
        max_X1 = self.ranges_of_variables[0][1]
        min_X2 = self.ranges_of_variables[1][0]
        max_X2 = self.ranges_of_variables[1][1]
        number_of_samples_of_domain = self.number_of_samples_of_domain

        plt.axis([min_X1, max_X1, min_X2, max_X2])
        ax = plt.gca()
        ax.set_autoscale_on(False)
        alpha_value = 1. / len(self.constraints)

        X1_linspace = np.linspace(min_X1, max_X1, num=number_of_samples_of_domain)
        X2_linspace = np.linspace(min_X2, max_X2, num=number_of_samples_of_domain)

        X1, X2 = np.meshgrid(X1_linspace, X2_linspace)

        def create_Z(x, y, function):
            new_point = Point([x, y])
            return function.value_at(new_point)

        Z = create_Z(X1, X2, self.function)

        plt.contour(X1, X2, Z, 3, colors='black')
        #add colour
        plt.imshow(Z, extent=[min_X1, max_X1, min_X2, max_X2], origin='lower', cmap=cmap, alpha=1)
        plt.colorbar();

        #plt.contourf(X1, X2, Z, 20, cmap='RdGy')
        #plt.colorbar();

        #TODO constraints

        data_of_constraints = []

        for constraint in self.constraints:
            if self.is_inequality_implicit_constraint(constraint):
                data_of_current_constraint = []
                Z_of_constraint = []
                for x2 in X2_linspace:
                    Z = []
                    for x1 in X1_linspace:
                        point = Point([x1, x2])
                        if (constraint.is_satisfied(point) is True):
                            Z.append(np.nan)
                        else:
                            Z.append(constraint.value_at(point))
                    Z_of_constraint.append(Z)
                X1_of_constraint, X2_of_constraint = np.meshgrid(X1_linspace, X2_linspace)

                # plot_this_constraint
                plt.contourf(X1_of_constraint, X2_of_constraint, Z_of_constraint, 20, cmap=constraints_cmap, alpha=alpha_value)
                plt.colorbar();

        #plt.plot(xRjesenja[iteration], yRjesenja[iteration], 'go')
        for point in self.points:
            plt.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1), 'go')
        plt.show()

    def is_inequality_implicit_constraint(self, constraint):
        for element in inspect.getmro(type(constraint)):
            if (
                    Constraints.IInequalityImplicitConstraint.IInequalityImplicitConstraint.__name__ == element.__name__ and Constraints.IInequalityImplicitConstraint.IInequalityImplicitConstraint.__module__ in element.__module__):
                return True
        return False

    def is_equality_implicit_constraint(self, constraint):
        for element in inspect.getmro(type(constraint)):
            if (
                    Constraints.IEqualityImplicitConstraint.IEqualityImplicitConstraint.__name__ == element.__name__ and Constraints.IEqualityImplicitConstraint.IEqualityImplicitConstraint.__module__ in element.__module__):
                return True
        return False

    #def draw_3D_graph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain, cmap):
    #def draw_3D_graph(self, cmap):
    def draw_3D_graph(self):
        plt.clf()
        plt.close('all')
        plt.figure(self.figure_number)
        ax = plt.axes(projection='3d')

        cmap = self.cmap
        min_X1 = self.ranges_of_variables[0][0]
        max_X1 = self.ranges_of_variables[0][1]
        min_X2 = self.ranges_of_variables[1][0]
        max_X2 = self.ranges_of_variables[1][1]
        number_of_samples_of_domain = self.number_of_samples_of_domain

        # region Create data for plotting the graph of the function
        X1_linspace = np.linspace(min_X1, max_X1, number_of_samples_of_domain)
        X2_linspace = np.linspace(min_X2, max_X2, number_of_samples_of_domain)

        X1_for_graph, X2_for_graph = np.meshgrid(X1_linspace, X2_linspace)
        Z_for_graph = []
        for x2 in X2_linspace:
            Z = []
            for x1 in X1_linspace:
                new_point = Point([x1, x2])
                Z.append(self.function.value_at(new_point))
            Z_for_graph.append(Z)
        # endregion

        #region Plot constraints
        for constraint in self.constraints:
            Z_of_constraint = []

            if self.is_equality_implicit_constraint(constraint):
                Z_of_constraint = self.create_graph_data_for_equality_implicit_constraint(X1_linspace, X2_linspace, constraint)
                for i in range(len(Z_for_graph)):
                    for j in range(len(Z_for_graph[i])):
                        if np.isnan(Z_of_constraint[i][j]):
                            # Z_for_graph should stay as it is
                            pass
                        else:
                            Z_for_graph[i][j] = np.nan
                ax.contour3D(X1_for_graph, X2_for_graph, Z_of_constraint, 50, cmap='autumn')

            elif self.is_inequality_implicit_constraint(constraint):
                Z_of_constraint = self.create_graph_data_for_inequality_implicit_constraint(X1_linspace, X2_linspace, constraint)
                for i in range(len(Z_for_graph)):
                    for j in range(len(Z_for_graph[i])):
                        if np.isnan(Z_of_constraint[i][j]):
                            # Z_for_graph should stay as it is
                            pass
                        else:
                            Z_for_graph[i][j] = np.nan
                ax.contour3D(X1_for_graph, X2_for_graph, Z_of_constraint, 50, cmap='autumn')
            else: #TODO explicit constraints?
                pass

            #Z_for_graph = self.remove_constrained_area_from_main_graph(Z_for_graph, Z_of_constraint)
        #endregion

        #region Plot graph of the function
        ax.contour3D(X1_for_graph, X2_for_graph, Z_for_graph, 50, cmap=cmap)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')
        #endregion

        #region Plot all points from internal list
        for point in self.points:
            #ax.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1), point.get_value_at_dimension(2), markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=1)
            ax.plot([point.get_value_at_dimension(0)], [point.get_value_at_dimension(1)], [self.function.value_at(point)], markerfacecolor='g', markeredgecolor='k', marker='o', markersize=5, alpha=1)
        #endregion

        plt.show()


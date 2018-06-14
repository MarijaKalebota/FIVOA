import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#from Point import *
#import Point
#from FIVOA.Point import *
import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Point import *
#from Point import Point
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
import numbers
from Constraints import *


class Drawer:
    '''
    def __init__(self, logger):
        self.logger = logger
        self.points = []
        self.constraints = []
        '''

    def __init__(self):
        self.points = []
        self.constraints = []

    def add_function(self, function):
        self.function = function

    def add_point(self, point):
        self.points.append(point)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

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
                        point = Point(2, [x1, x2])
                        Z.append(self.function.value_at(point))
                else:
                    if (constraint.is_satisfied(x2) is True):
                        Z.append(np.nan)
                    else:
                        point = Point(2, [x1, x2])
                        Z.append(self.function.value_at(point))
            Z_of_constraint.append(Z)
        return Z_of_constraint

    def create_graph_data_for_equality_implicit_constraint(self, X1_for_graph_before_meshgrid, X2_for_graph_before_meshgrid, constraint):
        Z_of_constraint = []
        for x2 in X2_for_graph_before_meshgrid:
            Z = []
            for x1 in X1_for_graph_before_meshgrid:
                point = Point(2, [x1, x2])
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
                point = Point(2, [x1, x2])
                if (constraint.is_satisfied(point) is True):
                    Z.append(np.nan)
                else:
                    # Z.append(constraint.value_at(matrix_x1_x2))
                    Z.append(self.function.value_at(point))
            Z_of_constraint.append(Z)
        return Z_of_constraint

    def draw_2D_graph(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
        plt.clf()
        plt.close('all')
        # TODO need this?
        #plt.figure(iteration)
        plt.axis([min_X1, max_X1, min_X2, max_X2])
        ax = plt.gca()
        ax.set_autoscale_on(False)

        X = np.linspace(min_X1, max_X1, num=number_of_samples_of_domain)
        X_points = []
        for x in X:
            new_point = Point(1, [x])
            X_points.append(new_point)
        #Y = [self.function.value_at(x) for x in X]
        #Y = [self.function.value_at(x) for x in X_points]
        Y = [self.function.value_at(Point(1, [x])) for x in X]
        plt.plot(X, Y, 'b')

        # TODO constraints

        #plt.plot(x_value_of_current_optimum, y_value_of_current_optimum, 'ro')
        for point in self.points:
            plt.plot(point.get_value_at_dimension(0), self.function.value_at(point), 'ro')
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
            return function.value_at(new_point)

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
                Z.append(self.function.value_at(new_point))
            Z_for_graph.append(Z)
        # endregion


        #print(self.constraints)
        # TODO constraints
        for constraint in self.constraints:
            print(constraint)
            print(type(constraint))
            print (type(constraint))
            print(issubclass(type(constraint), IInequalityImplicitConstraint.IInequalityImplicitConstraint))
            Z_of_constraint = []

            #if isinstance(constraint, IEqualityImplicitConstraint.IEqualityImplicitConstraint):
            if issubclass(type(constraint), IEqualityImplicitConstraint.IEqualityImplicitConstraint):
                #pass
                Z_of_constraint = self.create_graph_data_for_equality_implicit_constraint(X1_linspace, X2_linspace, constraint)
                for i in range(len(Z_for_graph)):
                    for j in range(len(Z_for_graph[i])):
                        if np.isnan(Z_of_constraint[i][j]):
                            # Z_for_graph should stay as it is
                            pass
                        else:
                            Z_for_graph[i][j] = np.nan
                ax.contour3D(X1_for_graph, X2_for_graph, Z_of_constraint, 50, cmap='autumn')
                #plt.show()
            #elif isinstance(constraint, IInequalityImplicitConstraint.IInequalityImplicitConstraint):
            #elif isinstance(constraint, InequalityImplicitConstraint1.InequalityImplicitConstraint1):
            elif issubclass(type(constraint), IInequalityImplicitConstraint.IInequalityImplicitConstraint):
                #pass
                Z_of_constraint = self.create_graph_data_for_inequality_implicit_constraint(X1_linspace, X2_linspace, constraint)
                for i in range(len(Z_for_graph)):
                    for j in range(len(Z_for_graph[i])):
                        if np.isnan(Z_of_constraint[i][j]):
                            # Z_for_graph should stay as it is
                            pass
                        else:
                            Z_for_graph[i][j] = np.nan
                ax.contour3D(X1_for_graph, X2_for_graph, Z_of_constraint, 50, cmap='autumn')

                print Z_of_constraint
                #plt.show()
            else: #TODO explicit constraints?
                #raise AssertionError(isinstance(constraint, IInequalityImplicitConstraint.IInequalityImplicitConstraint))
                print "else"
                pass

            #Z_for_graph = self.remove_constrained_area_from_main_graph(Z_for_graph, Z_of_constraint)

        # Plot fixed graph
        ax.contour3D(X1_for_graph, X2_for_graph, Z_for_graph, 50, cmap=cmap)
        # plt.plot([-1.9], [2.0], 'b')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')

        # Plot all points from internal list
        for point in self.points:
            #ax.plot(point.get_value_at_dimension(0), point.get_value_at_dimension(1), point.get_value_at_dimension(2), markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=1)
            ax.plot([point.get_value_at_dimension(0)], [point.get_value_at_dimension(1)], [self.function.value_at(point)], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=1)
        plt.show()


import numpy as np
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
import numbers
from Animator import *

class Presenter:
    def __init__(self, logger, drawer, animator):
        self.logger = logger
        self.drawer = drawer
        self.animator = animator

    #def present2(self):
        #create dropdown

    def draw_3D_iteration(self, iteration_number, X1_range, X2_range, number_of_samples_of_domain, cmap):
        self.drawer.clear_points()
        self.drawer.add_point(self.logger.get_iteration(iteration_number).get_current_solution())
        self.drawer.set_ranges_of_variables([X1_range, X2_range])
        self.drawer.set_number_of_samples_of_domain(number_of_samples_of_domain)
        self.drawer.set_cmap(cmap)
        self.drawer.set_figure_number(iteration_number)

        self.drawer.draw_3D_graph()

    def draw_contour_iteration(self, iteration_number, X1_range, X2_range, number_of_samples_of_domain, cmap, constraints_cmap):
        self.drawer.clear_points()
        self.drawer.add_point(self.logger.get_iteration(iteration_number).get_current_solution())
        self.drawer.set_ranges_of_variables([X1_range, X2_range])
        self.drawer.set_number_of_samples_of_domain(number_of_samples_of_domain)
        self.drawer.set_cmap(cmap)
        self.drawer.set_constraints_cmap(constraints_cmap)
        self.drawer.set_figure_number(iteration_number)

        self.drawer.draw_contour_graph()


    def present_contour(self):
        function = self.logger.get_function()
        number_of_iterations = self.logger.get_number_of_iterations()

        # region Define colormap choices
        colormap_choices = {
            'GnBu': 'GnBu',
            'Greens': 'Greens'}  # ,

        constraints_colormap_choices = {
            'autumn': 'autumn',
            'copper': 'copper'}

        # endregion

        # region Create and link widgets
        iteration_slider = self.animator.create_int_slider(min=0, max=number_of_iterations - 1, step=1, value=0)
        play, next_button, previous_button = self.animator.create_play_widget_with_next_and_previous_buttons(number_of_iterations)
        widgets.jslink((play, 'value'), (iteration_slider, 'value'))

        X1_range_slider = self.animator.create_int_range_slider(value = self.drawer.get_range_of_variable(0), description= "X1 range:")
        X2_range_slider = self.animator.create_int_range_slider(value = self.drawer.get_range_of_variable(1), description= "X2 range:")
        number_of_samples_of_domain_text_box = self.animator.create_bounded_int_text_box(value=self.drawer.get_number_of_samples_of_domain(), description= "Number of samples of domain: ")
        colormap_choices_dropdown = self.animator.create_dropdown(options=colormap_choices, description= "Colormap choices:")
        constraints_colormap_choices_dropdown = self.animator.create_dropdown(options=constraints_colormap_choices,
                                                                  description="Constraints colormap choices:")

        # endregion

        interact(self.draw_contour_iteration, iteration_number=iteration_slider, X1_range = X1_range_slider, X2_range = X2_range_slider, number_of_samples_of_domain = number_of_samples_of_domain_text_box, cmap = colormap_choices_dropdown, constraints_cmap = constraints_colormap_choices_dropdown)

        # region Call the function interactively
        #interact(self.drawer.draw_3D_graph, iteration_number=iteration_slider, cmap=cmap_choices)
        # endregion
        # region Display remaining widgets
        display(play)
        display(previous_button)
        display(next_button)
        # endregion


    #def present_3D(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
    def present_3D(self):
        function = self.logger.get_function()
        number_of_iterations = self.logger.get_number_of_iterations()

        # region Define colormap choices
        colormap_choices = {
            'Accent': 'Accent',
            'Accent_r': 'Accent_r'}  # ,

        '''
            'Blues': 'Blues',
            'Blues_r': 'Blues_r',
            'BrBG' : 'BrBG',
            'BrBG_r' : 'BrBG_r',
            'BuGn' : 'BuGn',
            'BuGn_r' : 'BuGn_r'
        }'''
        # endregion

        # region Create and link widgets
        #w = widgets.IntSlider(min=0, max=number_of_iterations - 1, step=1, value=0)
        iteration_slider = self.animator.create_int_slider(min=0, max=number_of_iterations - 1, step=1, value=0)
        play, next_button, previous_button = self.animator.create_play_widget_with_next_and_previous_buttons(number_of_iterations)
        widgets.jslink((play, 'value'), (iteration_slider, 'value'))

        X1_range_slider = self.animator.create_int_range_slider(value = self.drawer.get_range_of_variable(0), description= "X1 range:")
        X2_range_slider = self.animator.create_int_range_slider(value = self.drawer.get_range_of_variable(1), description= "X2 range:")
        number_of_samples_of_domain_text_box = self.animator.create_bounded_int_text_box(value=self.drawer.get_number_of_samples_of_domain(), description= "Number of samples of domain: ")
        colormap_choices_dropdown = self.animator.create_dropdown(options=colormap_choices, description= "Colormap choices:")
        # endregion

        interact(self.draw_3D_iteration, iteration_number=iteration_slider, X1_range = X1_range_slider, X2_range = X2_range_slider, number_of_samples_of_domain = number_of_samples_of_domain_text_box, cmap = colormap_choices_dropdown)

        # region Call the function interactively
        #interact(self.drawer.draw_3D_graph, iteration_number=iteration_slider, cmap=cmap_choices)
        # endregion
        # region Display remaining widgets
        display(play)
        display(previous_button)
        display(next_button)
        # endregion




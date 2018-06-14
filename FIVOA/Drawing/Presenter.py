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


    def present_3D(self, min_X1, max_X1, min_X2, max_X2, number_of_samples_of_domain):
        function = self.logger.get_function()

        # region Create fixed arrays for data from logger
        play_max_of_interval = 0
        X1_from_logger = []
        X2_from_logger = []
        Z_from_logger = []

        number_of_iterations = self.logger.get_number_of_iterations()

        for iteration_number in range(number_of_iterations):
            iteration = self.logger.get_iteration(iteration_number)
            #X1_from_logger.append(iteration.x1Value)
            X1_from_logger.append(iteration.get_current_solution.get_value_at_dimension(0))
            X2_from_logger.append(iteration.get_current_solution.get_value_at_dimension(1))
            Z_from_logger.append(iteration.get_function_value())
            # endregion

        # region Create and link widgets
        w = widgets.IntSlider(min=0, max=play_max_of_interval - 1, step=1, value=0)
        play, next_button, previous_button = self.animator.create_play_widget_with_next_and_previous_buttons(number_of_iterations)
        widgets.jslink((play, 'value'), (w, 'value'))
        # endregion

        # region Define cmap choices
        cmap_choices = {
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

        # region Call the function interactively
        interact(self.drawer.draw_2D_graph, iteration_number=w, cmap=cmap_choices)
        # endregion
        # region Display remaining widgets
        display(play)
        display(previous_button)
        display(next_button)
        # endregion




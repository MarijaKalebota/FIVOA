from Animator import *
class Presenter:
    def __init__(self, logger, drawer, animator):
        self.logger = logger
        self.drawer = drawer
        self.animator = animator

    def draw_2D_iteration(self, iteration_number):
        self.drawer.clear_points()
        self.drawer.add_point(self.logger.get_iteration(iteration_number).get_current_solution())
        self.drawer.draw_2D_graph()

    def present(self):
        function = self.logger.get_function()
        self.drawer.add_function(function)
        number_of_iterations = self.logger.get_number_of_iterations()
        iteration_slider = self.animator.create_int_slider(min=0, max=number_of_iterations - 1, step=1)

        interact(self.draw_2D_iteration, iteration_number=iteration_slider)
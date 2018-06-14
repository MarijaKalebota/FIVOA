import ipywidgets as widgets
from ipywidgets import *

class Animator:
    def __init__(self):
        pass

    #def create_slider(self, ):

    def create_play_widget_with_next_and_previous_buttons(self, play_max_of_interval):
        play = widgets.Play(
            value=0,
            min=0,
            max=play_max_of_interval,
            step=1,
            description="Press play",
            disabled=False
        )
        nextButton = widgets.Button(description="Next")
        previousButton = widgets.Button(description="Previous")

        def on_nextButton_clicked(x):
            if (play.value < play.max):
                play.value += 1

        def on_previousButton_clicked(x):
            if (play.value > 0):
                play.value -= 1

        nextButton.on_click(on_nextButton_clicked)
        previousButton.on_click(on_previousButton_clicked)

        return play, nextButton, previousButton
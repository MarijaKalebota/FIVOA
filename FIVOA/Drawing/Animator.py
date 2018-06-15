import ipywidgets as widgets
from ipywidgets import *

class Animator:
    def __init__(self):
        pass

    def create_int_slider(self, value=7, min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
        return widgets.IntSlider(value=value, min = min, max = max, step = step, description = description, disabled = disabled, continuous_update = continuous_update, orientation = orientation, readout = readout, readout_format = readout_format)

    def create_int_range_slider(self, value=[5, 7], min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
        return widgets.IntRangeSlider(value=value, min = min, max = max, step = step, description = description, disabled = disabled, continuous_update = continuous_update, orientation = orientation, readout = readout, readout_format = readout_format)

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
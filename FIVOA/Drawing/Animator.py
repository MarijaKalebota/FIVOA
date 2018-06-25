import ipywidgets as widgets
from ipywidgets import *

class Animator:
    def __init__(self):
        pass

    def create_int_slider(self, value=7, min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
        return widgets.IntSlider(value=value, min = min, max = max, step = step, description = description, disabled = disabled, continuous_update = continuous_update, orientation = orientation, readout = readout, readout_format = readout_format)

    def create_int_range_slider(self, value=[5, 7], min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
        min = value[0] - (value[1] - value[0])
        max = value[1] + (value[1] - value[0])
        return widgets.IntRangeSlider(value=value, min = min, max = max, step = step, description = description, disabled = disabled, continuous_update = continuous_update, orientation = orientation, readout = readout, readout_format = readout_format)

    def create_bounded_int_text_box(self, value=150, min=0, max=1000, step=1, description='Text:', disabled=False, style = {'description_width': 'initial'}):
        return widgets.BoundedIntText(value=value, min=min, max = max, step = step, description=description, disabled = disabled, style = style)

    def create_dropdown(self, options={'Option 1': 'Value 1', 'Option 2': 'Value 2', 'Option 3': 'Value 3'}, value='Value 2', description='Dropdown options:'):
        value = options.values()[0]
        return widgets.Dropdown(options = options, value= value, description = description)

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
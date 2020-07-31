from gpiozero import Button, LED
from ..display import gui
import time


def start():
    orange_started = False
    orange_pedal_primed = False
    orange_finished = False
    orange_button = Button()  # GPIO pin for orange finish button
    orange_pedal = Button()  # GPIO pin for orange start pedal

    grey_started = False
    grey_pedal_primed = False
    grey_finished = False
    grey_button = Button()  # GPIO pin for grey finish button
    grey_pedal = Button()  # GPIO pin for grey start pedal

    while 1:
        # Check for finish
        if orange_started:
            if orange_button.is_pressed:
                orange_final_time = time.time()
                orange_finished = True
        if grey_started:
            if grey_button.is_pressed:
                grey_final_time = time.time()
                grey_finished = True

        # Check for start/prime
        if orange_pedal_primed:
            if not orange_pedal.is_pressed:
                orange_initial_time = time.time()
                orange_started = True
                orange_pedal_primed = False
        else:
            if orange_pedal.is_pressed:
                orange_pedal_primed = True
        # same but for grey
        if grey_pedal_primed:
            if not grey_pedal.is_pressed:
                grey_initial_time = time.time()
                grey_started = True
                grey_pedal_primed = False
        else:
            if grey_pedal.is_pressed:
                grey_pedal_primed = True

        # get current times
        if orange_finished:
            orange_time = orange_final_time - orange_initial_time
        else:
            orange_time = time.time() - orange_initial_time
        if grey_finished:
            grey_time = grey_final_time - grey_initial_time
        else:
            grey_time = time.time() - grey_initial_time

        # display times
        gui.display_orange_time(orange_time)
        gui.display_grey_time(grey_time)

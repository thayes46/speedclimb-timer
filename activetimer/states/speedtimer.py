from gpiozero import Button, LED
from ..display import gui
import time

exit_program = False

orange_started = False
orange_pedal_primed = False
orange_finished = False
orange_initial_time = 0
orange_final_time = 0
orange_time = 0
orange_button = Button()  # GPIO pin for orange finish button
orange_pedal = Button()  # GPIO pin for orange start pedal
orange_lights = LED()  # GPIO pin for orange flashy flashies

grey_started = False
grey_pedal_primed = False
grey_finished = False
grey_initial_time = 0
grey_final_time = 0
grey_time = 0
grey_button = Button()  # GPIO pin for grey finish button
grey_pedal = Button()  # GPIO pin for grey start pedal
grey_lights = LED()  # GPIO pin for grey flashy flashies


def start():
    global orange_started
    global orange_pedal_primed
    global orange_finished
    global orange_initial_time
    global orange_final_time
    global orange_time
    global grey_started
    global grey_pedal_primed
    global grey_finished
    global grey_initial_time
    global grey_final_time
    global grey_time
    timing_window = gui.start_timing_window()
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
        timing_window.display_orange_time(orange_time)
        timing_window.display_grey_time(grey_time)

        # Lightshow for winner
        if orange_finished and grey_finished:
            if orange_time < grey_time:
                # orange won
                orange_lights.blink(on_time=0.125, off_time=0.125,
                                    fade_in_time=0, fade_out_time=0, n=20,
                                    background=True)
            else:
                # grey won
                grey_lights.blink(on_time=0.125, off_time=0.125,
                                  fade_in_time=0, fade_out_time=0, n=20,
                                  background=True)
            time.sleep(10)
            reset_lanes()


def reset_lanes():
    global orange_started
    global orange_pedal_primed
    global orange_finished
    global orange_initial_time
    global orange_final_time
    global orange_time
    global grey_started
    global grey_pedal_primed
    global grey_finished
    global grey_initial_time
    global grey_final_time
    global grey_time
    orange_started = False
    orange_pedal_primed = False
    orange_finished = False
    orange_initial_time = 0
    orange_final_time = 0
    orange_time = 0
    grey_started = False
    grey_pedal_primed = False
    grey_finished = False
    grey_initial_time = 0
    grey_final_time = 0
    grey_time = 0

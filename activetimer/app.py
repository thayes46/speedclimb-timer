from .states import speedtimer, default
from .display import records, gui
from gpiozero import Button
import time

# Ensure these values are the same in .states/speedtimer.py
orange_pedal = Button()  # GPIO pin for orange start pedal
grey_pedal = Button()  # GPIO pin for orange start pedal


# Running total of hours worked on this for fun:
# 19

from .display import gui
def run():

    leaderboard = gui.start_leaderboard_window()
    while 1:  # it's always doing one of these
        default.run()
        # display slideshow and leaderboard
        while not (orange_pedal.is_pressed and grey_pedal.is_pressed):
            # wait until there's an update from the pedals
            time.sleep(1)
            pass
        speedtimer.start()
        # start() only returns when timing loop ends and window closes

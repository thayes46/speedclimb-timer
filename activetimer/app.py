from .states import running, default
from .display import records, gui
from gpiozero import Button
import time

# Ensure these values are the same in .states/speedtimer.py
orange_pedal = Button(21)  # GPIO pin for orange start pedal
grey_pedal = Button(20)  # GPIO pin for orange start pedal


# Running total of hours worked on this for fun:
# 22

def run():
    """
    gui.display_leaders()
    while 1:  # it's always doing one of these
        running.stop()
        default.run()
        # display slideshow and leaderboard
        while not (orange_pedal.is_pressed and grey_pedal.is_pressed):
            # wait until there's an update from the pedals
            time.sleep(3)
            pass
    default.stop()
    """
    running.run()

from .states import speedtimer, default
from .display import records
from gpiozero import Button

# Ensure these values are the same in .states/speedtimer.py
orange_pedal = Button()  # GPIO pin for orange start pedal
grey_pedal = Button()  # GPIO pin for orange start pedal


# Running total of hours worked on this for fun:
# 12

def run():
    while 1:  # it's always doing one of these
        top_times = records.get_records()
        default.run()
        # display slideshow and leaderboard
        while 1:  # TODO: replace 1 with foot pedal checks to start
            # wait until there's an update from the pedals
            pass
        speedtimer.start()
        while 1:  # TODO: replace 1 with foot pedal checks to end
            # run timers
            pass

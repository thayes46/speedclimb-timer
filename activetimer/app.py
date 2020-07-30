from .timing import speedtimer
from .display import records


def run():
    while 1: # it's always doing one of these
        top_times = records.get_records()
        while 1:  # TODO: replace 1 with foot pedal checks to start
            # display slideshow and leaderboard
            pass
        while 1:  # TODO: replace 1 with foot pedal checks to end
            # run timers
            pass

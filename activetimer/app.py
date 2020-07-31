from .states import speedtimer, default
from .display import records


def run():
    while 1: # it's always doing one of these
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

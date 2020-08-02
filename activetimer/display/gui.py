from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# from .records import get_records


def start_leaderboard_window():
    # return window with timers
    leaderboard_window = LeaderBoardWindow()
    return leaderboard_window


class LeaderBoardWindow(QMainWindow):
    # TODO: implement
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leaderboards")
        self.setGeometry(100, 100, 400, 500)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.top_times = get_records()

def display_leaders():
    # TODO: implement
    pass

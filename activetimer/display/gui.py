from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..states import speedtimer
from ..states.speedtimer import exit_program, orange_time, grey_time
import sys
import time

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


# TODO: display slideshow
# TODO: get the display to update

App = QApplication(sys.argv)
window = TimingWindow()
window.show()
App.exec_()

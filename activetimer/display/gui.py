import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# from .records import get_records


def start_timing_window():
    # return window with timers
    # TODO: test this execution with both leaderboard and timing
    timing_window = TimingWindow()
    return timing_window


class TimingWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        # Timer takes up top half of screen
        self.setGeometry(0, 0, 1080, 960)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # Times
        self.orange_time = 0
        self.grey_time = 0

        # The labels to display
        self.orange_label = QLabel(self)
        self.grey_label = QLabel(self)

        self.orange_label.setGeometry(0, 0, 1080, 480)
        self.grey_label.setGeometry(0, 480, 1080, 480)

        # TODO: make style decent
        self.orange_label.setStyleSheet("border : 4px solid black;")
        self.grey_label.setStyleSheet("border : 4px solid black;")

        self.orange_label.setText(str(self.orange_time))
        self.grey_label.setText(str(self.grey_time))

        self.orange_label.setFont(QFont('Arial', 25))  # TODO: make text beeg
        self.grey_label.setFont(QFont('Arial', 25))  # TODO: make text beeg

        self.orange_label.setAlignment(Qt.AlignCenter)
        self.grey_label.setAlignment(Qt.AlignCenter)

    def update_orange_time(self, orange_updated_time):
        self.orange_time = orange_updated_time
        self.orange_label.setText(str(self.orange_time))

    def update_grey_time(self, grey_updated_time):
        self.grey_time = grey_updated_time
        self.grey_label.setText(str(self.grey_time))


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

timing_app = QApplication(sys.argv)
window = start_timing_window()
sys.exit(timing_app)


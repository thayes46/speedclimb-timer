from PyQt5.QtWidgets import *


def start_timing_window():
    # return window with timers
    timing_window = Window()
    return timing_window


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        self.setGeometry(100, 100, 400, 500)

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

        self.orange_label.setGeometry()  # TODO: set geometry
        self.grey_label.setGeometry()  # TODO: set geometry

        self.orange_label.setStyleSheet()  # TODO: style
        self.grey_label.setStyleSheet()  # TODO: style

        self.orange_label.setText(str(self.orange_time))
        self.grey_label.setText(str(self.grey_time))

        self.orange_label.setFont('Arial', 25)  # TODO: make text beeg
        self.grey_label.setFont('Arial', 25)  # TODO: make text beeg

        self.orange_label.setAlignment()  # TODO: play with alignment
        self.grey_label.setAlignment()  # TODO: play with alignment

    def update_orange_time(self, orange_updated_time):
        self.orange_time = orange_updated_time
        self.orange_label.setText(str(self.orange_time))

    def update_grey_time(self, grey_updated_time):
        self.grey_time = grey_updated_time
        self.grey_label.setText(str(self.grey_time))

# TODO: make leaderboard
# TODO: display slideshow

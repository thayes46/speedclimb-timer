import time
from gpiozero import Button, LED
from .display import records
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Running total of hours worked on this for fun:
# 59

def run():
    while 1:
        # Logic for when to kick out based on buttons being pushed is handled
        # in each running widget respectively
        # display_leaders()
        # Eventually also have slideshow here
        display_timer()


"""
I really didn't want to make this a megascript, however the Pi GPIO can only
be called from 1 python script so that lumps pretty much everything to be
stuck together
"""

"""
To add back in on deploy to pi
orange_button = Button(24)  # GPIO pin for orange finish button
orange_pedal = Button(21)  # GPIO pin for orange start pedal
orange_lights = LED(23)  # GPIO pin for orange flashy flashies
grey_button = Button(14)  # GPIO pin for grey finish button
grey_pedal = Button(20)  # GPIO pin for grey start pedal
grey_lights = LED(15) # GPIO pin for grey flashy flashies
"""
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


class TimingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("starting")
        self.timing_widget = TimingWidget()
        self.timing_widget.show()

        # Dummy timer to give the widget time to get going
        self.dummy_timer = QTimer()
        self.dummy_timer.setSingleShot(True)
        self.dummy_timer.setInterval(225)
        # function connected to is the startup
        self.dummy_timer.timeout.connect(self.woah_nelly)
        self.dummy_timer.start()

    # startup function for widget/thread
    def woah_nelly(self):
        # main method of timers
        # Recursive boolean to imitate thread
        while self.timing_widget.begin():
            # Need to process signals to get any update
            QApplication.processEvents()

            # Restricting counter to update every 1/2 second. Arbitrary
            time.sleep(0.5)
        QApplication.processEvents()
        self.timing_widget.yeet()
        self.timing_widget.destroy()


def reset_lanes():
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


class TimingWidget(QWidget):
    # GUI for timers
    def __init__(self):
        super(TimingWidget, self).__init__()

        # setting title
        self.grey_label = QLabel(self)
        self.orange_label = QLabel(self)
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        # Timer takes up top half of screen
        self.setGeometry(0, 0, 1080, 960)

        # setup UI
        self.UiComponents()

        # potentially arbitrary
        self.dummy_counter = 1

    def begin(self):
        print("Updating times")
        self.update_orange_time(self.dummy_counter)
        self.dummy_counter = self.dummy_counter + 1
        return_value = self.dummy_counter < 10
        return return_value

    # method for widgets
    def UiComponents(self):
        # give labels their juice
        self.orange_label.setGeometry(0, 0, 1080, 480)
        self.grey_label.setGeometry(0, 480, 1080, 480)

        # TODO: make style decent
        self.orange_label.setStyleSheet("border : 16px solid orange;")
        self.grey_label.setStyleSheet("border : 16px solid grey;")

        self.orange_label.setText(str(orange_time))
        self.grey_label.setText(str(grey_time))

        self.orange_label.setFont(QFont('Arial', 25))  # TODO: make text beeg
        self.grey_label.setFont(QFont('Arial', 25))  # TODO: make text beeg

        self.orange_label.setAlignment(Qt.AlignCenter)
        self.grey_label.setAlignment(Qt.AlignCenter)

    def update_orange_time(self, orange_updated_time):
        self.orange_label.setText(str(orange_updated_time))

    def update_grey_time(self, grey_updated_time):
        self.grey_label.setText(str(grey_updated_time))

    def yeet(self):
        self.close()


# class DefaultWidget(QWidget):
# default slideshow + leaderboard

def display_timer():
    reset_lanes()
    app = QApplication([])
    window = TimingWindow()
    app.exec_()


def display_leaders():
    # TODO: implement
    pass

import time
from gpiozero import Button, LED
# from .display import records
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Running total of hours worked on this for fun:
# 62

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
stuck togeth
"""

# To add back in on deploy to pi
# orange_button = Button(24)  # GPIO pin for orange finish button
# orange_pedal = Button(21)  # GPIO pin for orange start pedal
# orange_lights = LED(23)  # GPIO pin for orange flashy flashies
# grey_button = Button(14)  # GPIO pin for grey finish button
# grey_pedal = Button(20)  # GPIO pin for grey start pedal
# grey_lights = LED(15)  # GPIO pin for grey flashy flashies


# test putting both to pedals


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
        self.timing_widget.begin()
        QApplication.processEvents()
        self.timing_widget.yeet()
        self.timing_widget.destroy()


def reset_lanes():
    dummy_time = time.time()
    orange_started = False
    orange_pedal_primed = False
    orange_finished = False
    orange_initial_time = dummy_time
    orange_final_time = dummy_time
    orange_time = dummy_time
    grey_started = False
    grey_pedal_primed = False
    grey_finished = False
    grey_initial_time = dummy_time
    grey_final_time = dummy_time
    grey_time = dummy_time


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
        self.stop_timer = False
        # test setup
        self.orange_pedal = Button(21)  # orange pedal
        self.orange_button = Button(20)  # grey pedal

        self.grey_pedal = Button(24)
        self.grey_button = Button(14)
        self.orange_lights = LED(23)
        self.grey_lights = LED(15)

        self.orange_started = False
        self.orange_pedal_primed = False
        self.orange_finished = False
        self.orange_initial_time = 0
        self.orange_final_time = 0
        self.orange_time = 0
        self.grey_started = False
        self.grey_pedal_primed = False
        self.grey_finished = False
        self.grey_initial_time = 0
        self.grey_final_time = 0
        self.grey_time = 0



    def begin(self):
        self.run()

    # method for widgets
    def UiComponents(self):
        # give labels their juice
        self.orange_label.setGeometry(0, 0, 1080, 480)
        self.grey_label.setGeometry(0, 480, 1080, 480)

        # TODO: make style decent
        self.orange_label.setStyleSheet("border : 16px solid orange;")
        self.grey_label.setStyleSheet("border : 16px solid grey;")

        self.orange_label.setText("0.000")
        self.grey_label.setText("0.000")

        self.orange_label.setFont(QFont('Arial', 60))  # TODO: make text beeg
        self.grey_label.setFont(QFont('Arial', 60))  # TODO: make text beeg

        self.orange_label.setAlignment(Qt.AlignCenter)
        self.grey_label.setAlignment(Qt.AlignCenter)

    def update_orange_time(self, orange_updated_time):
        self.orange_label.setText(str(orange_updated_time))

    def update_grey_time(self, grey_updated_time):
        self.grey_label.setText(str(grey_updated_time))

    def yeet(self):
        self.close()

    def run(self):
        while not self.stop_timer:
            QApplication.processEvents()
            # Main program loop
            # TODO: add a way to set stop timer to false,
            #   git out and kill window

            # Check for finish
            if self.orange_started:
                if self.orange_button.is_pressed:
                    self.orange_final_time = time.time()
                    self.orange_finished = True
            if self.grey_started:
                if self.grey_button.is_pressed:
                    self.grey_final_time = time.time()
                    self.grey_finished = True

            # Check for start/prime
            if self.orange_pedal_primed:
                if not self.orange_pedal.is_pressed:
                    self.orange_initial_time = time.time()
                    self.orange_started = True
                    self.orange_pedal_primed = False
            else:
                if self.orange_pedal.is_pressed:
                    self.orange_pedal_primed = True
            # same but for grey
            if self.grey_pedal_primed:
                if not self.grey_pedal.is_pressed:
                    self.grey_initial_time = time.time()
                    self.grey_started = True
                    self.grey_pedal_primed = False
            else:
                if self.grey_pedal.is_pressed:
                    self.grey_pedal_primed = True

            # get current times
            if self.orange_finished:
                self.orange_time = self.orange_final_time - \
                              self.orange_initial_time
            elif self.orange_started:
                print("updating orange")
                self.orange_time = time.time() - self.orange_initial_time
            if self.grey_finished:
                self.grey_time = self.grey_final_time - self.grey_initial_time
            elif self.grey_started:
                self.grey_time = time.time() - self.grey_initial_time

            # display times
            self.update_orange_time('{:.3f}'.format(self.orange_time))
            self.update_grey_time('{:.3f}'.format(self.grey_time))


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


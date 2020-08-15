import time
from gpiozero import Button, LED
# from .display import records
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Running total of hours worked on this for fun:
# 64

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


class TimingWidget(QWidget):
    # GUI for timers
    def __init__(self):
        super(TimingWidget, self).__init__()

        # setting title
        self.grey_label = QLabel(self)
        self.orange_label = QLabel(self)
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        # Timer takes up all of screen
        self.setGeometry(0, 0, 1920, 1040)

        # setup UI
        self.UiComponents()

        # potentially arbitrary
        self.dummy_counter = 1
        self.stop_timer = False

        # GPIO initialization
        self.orange_button = Button(24, False)  # GPIO pin for orange finish
        self.orange_pedal = Button(21, False)  # GPIO pin for orange start
        self.orange_lights = LED(23)  # GPIO pin for orange flashy flashies
        self.grey_button = Button(14, False)  # GPIO pin for grey finish button
        self.grey_pedal = Button(20, False)  # GPIO pin for grey start pedal
        self.grey_lights = LED(15)  # GPIO pin for grey flashy flashies

        # runtime variable initialization
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

        # test setup for reference if need be
        # self.orange_pedal = Button(21, False)  # orange pedal
        # self.orange_pedal.when_pressed = self.set_orange_start
        # self.orange_button = Button(20, False)  # grey pedal

        # self.grey_pedal = Button(24, False)
        # self.grey_button = Button(14, False)
        # self.orange_lights = LED(23)
        # self.grey_lights = LED(15)

    def begin(self):
        self.run()

    # method for widgets
    def UiComponents(self):
        # give labels their juice
        self.orange_label.setGeometry(0, 0, 1920, 520)
        self.grey_label.setGeometry(0, 520, 1920, 520)

        # TODO: make style decent
        self.orange_label.setStyleSheet("border : 40px solid orange;")
        self.grey_label.setStyleSheet("border : 40px solid grey;")

        self.orange_label.setText("0.000")
        self.grey_label.setText("0.000")

        self.orange_label.setFont(QFont('Arial', 80))  # TODO: make text beeg
        self.grey_label.setFont(QFont('Arial', 80))  # TODO: make text beeg

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
                    self.orange_started = False
            if self.grey_started:
                if self.grey_button.is_pressed:
                    self.grey_final_time = time.time()
                    self.grey_finished = True
                    self.grey_started = False

            # Check for start/prime
            if self.orange_pedal_primed:
                if not self.orange_pedal.is_pressed:
                    self.orange_initial_time = time.time()
                    self.orange_started = True
                    self.orange_pedal_primed = False
            else:
                if self.orange_pedal.is_pressed:
                    self.orange_pedal_primed = True
                    self.orange_finished = False
            # same but for grey
            if self.grey_pedal_primed:
                if not self.grey_pedal.is_pressed:
                    self.grey_initial_time = time.time()
                    self.grey_started = True
                    self.grey_pedal_primed = False
            else:
                if self.grey_pedal.is_pressed:
                    self.grey_pedal_primed = True
                    self.grey_finished = False

            # get current times
            if self.orange_finished:
                self.orange_time = self.orange_final_time - \
                                   self.orange_initial_time
            elif self.orange_started:
                self.orange_time = time.time() - self.orange_initial_time
            else:
                self.orange_time = 0
            if self.grey_finished:
                self.grey_time = self.grey_final_time - self.grey_initial_time
            elif self.grey_started:
                self.grey_time = time.time() - self.grey_initial_time
            else:
                self.grey_time = 0

            # display times
            self.update_orange_time('{:.3f}'.format(self.orange_time))
            self.update_grey_time('{:.3f}'.format(self.grey_time))

    # lambda for interrupt based loop
    # def set_orange_start(self):
    #     self.orange_started = True
    #     self.orange_initial_time = time.time()


# class DefaultWidget(QWidget):
# default slideshow + leaderboard

def display_timer():
    app = QApplication([])
    window = TimingWindow()
    app.exec_()


def display_leaders():
    # TODO: implement
    pass

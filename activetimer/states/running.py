import time
from gpiozero import Button, LED
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.threadactive = True
        self.stop_timer = False

        self.orange_started = False
        self.orange_pedal_primed = False
        self.orange_finished = False
        self.orange_initial_time = 0
        self.orange_final_time = 0
        self.orange_time = 0
        self.orange_button = Button(24)  # GPIO pin for orange finish button
        self.orange_pedal = Button(21)  # GPIO pin for orange start pedal
        self.orange_lights = LED(23)  # GPIO pin for orange flashy flashies

        self.grey_started = False
        self.grey_pedal_primed = False
        self.grey_finished = False
        self.grey_initial_time = 0
        self.grey_final_time = 0
        self.grey_time = 0
        self.grey_button = Button(14)  # GPIO pin for grey finish button
        self.grey_pedal = Button(20)  # GPIO pin for grey start pedal
        self.grey_lights = LED(15)  # GPIO pin for grey flashy flashies

        self.timing_window = TimingWindow()
        self.timing_window.show()

    def run(self):
        while not self.stop_timer:
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
            else:
                self.orange_time = time.time() - self.orange_initial_time
            if self.grey_finished:
                self.grey_time = self.grey_final_time - self.grey_initial_time
            else:
                self.grey_time = time.time() - self.grey_initial_time

            # display times
            self.timing_window.update_orange_time(self.orange_time)
            self.timing_window.update_grey_time(self.grey_time)

            # Lightshow for winner
            if self.orange_finished and self.grey_finished:
                if self.orange_time < self.grey_time:
                    # orange won
                    self.orange_lights.blink(on_time=0.125, off_time=0.125,
                                             fade_in_time=0, fade_out_time=0,
                                             n=20,
                                             background=True)
                else:
                    # grey won
                    self.grey_lights.blink(on_time=0.125, off_time=0.125,
                                           fade_in_time=0, fade_out_time=0,
                                           n=20,
                                           background=True)
                time.sleep(10)
                self.reset_lanes(self)
        self.timing_window.yeet()

    def reset_lanes(self):
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

    def stop(self):
        self.threadactive = False
        self.wait()


class TimingWindow(QMainWindow):

    def __init__(self):
        super(TimingWindow, self).__init__()

        # setting title
        self.grey_label = QLabel(self)
        self.orange_label = QLabel(self)
        self.grey_time = 0
        self.orange_time = 0
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        # Timer takes up top half of screen
        self.setGeometry(0, 0, 1080, 960)

        # calling method
        self.UiComponents()

    # method for widgets
    def UiComponents(self):
        # give labels their juice
        self.orange_label.setGeometry(0, 0, 1080, 480)
        self.grey_label.setGeometry(0, 480, 1080, 480)

        # TODO: make style decent
        self.orange_label.setStyleSheet("border : 16px solid orange;")
        self.grey_label.setStyleSheet("border : 16px solid grey;")

        self.orange_label.setText(str(self.orange_time))
        self.grey_label.setText(str(self.grey_time))

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


timing_thread = None


def run():
    timing_app = QApplication([])
    global timing_thread
    timing_thread = Main()
    timing_thread.start()
    timing_app.exec_()


def stop():
    global timing_thread
    if timing_thread is not None:
        timing_thread.stop()

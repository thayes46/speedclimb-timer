import sys, time
from gpiozero import Button, LED
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
Let's do this.... again.
I guess you could call it, redoing it
Rewrite for utilization of Qt threading
"""


class Main(QThread):
    def __init__(self):
        QThread.__init__(self)
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
            time.sleep(2)
            self.timing_window.update_grey_time(1)
            time.sleep(2)
            self.timing_window.update_orange_time(3)
            time.sleep(5)
            self.stop_timer = True


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


def run():
    timing_app = QApplication([])
    timing_thread = Main()
    timing_thread.start()
    timing_app.exec_()

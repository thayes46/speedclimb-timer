import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

"""
To add back in after testing
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("starting")
        self.timing_widget = TimingWindow()
        self.timing_widget.show()
        time.sleep(1)
        self.timing_widget.begin()

    def woah_nelly(self):
        print("woah nelly")
        self.timing_widget.begin()
        print("settle down now")
        self.timing_widget.yeet()
        self.destroy()


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


class TimingThread(QThread):
    # Thread running timer logic
    def __init__(self):
        QThread.__init__(self)
        reset_lanes()
        self.stop_timer = False

    def go(self, TimingWindow):
        # loop
        print("Starting main loop")
        while not self.stop_timer:
            time.sleep(2)
            TimingWindow.update_orange_time(1)
            time.sleep(2)
            self.stop_timer = True
        print("done with loop")


class TimingWindow(QWidget):
    # GUI for timers
    def __init__(self):
        super(TimingWindow, self).__init__()

        # setting title
        self.grey_label = QLabel(self)
        self.orange_label = QLabel(self)
        self.setWindowTitle("Orange and Grey lanes")

        # setting window geometry
        # Timer takes up top half of screen
        self.setGeometry(0, 0, 1080, 960)

        # setup UI
        self.UiComponents()

    def begin(self):
        self.update_grey_time(1)
        time.sleep(1)

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


# class DefaultThread(QThread):
# Thread for slideshow

# class DefaultWindow(QWidget):
# keeping here just in case

# def Main():
app = QApplication([])
main_window = MainWindow()
app.exec_()

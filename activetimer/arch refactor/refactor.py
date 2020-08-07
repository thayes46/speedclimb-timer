from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication
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

class MainCaller():
    def __init__(self):
        # timing_thread = TimingThread()
        # timing_thread.finished.connect(timing_thread.window.destroy())
        # timing_thread.start()


class TimingThread(QThread):
    # Thread running timer logic
    def __init__(self):
        QThread.__init__(self)
        self.stop_timer = False
        self.timing_window = TimingWindow()
        self.timing_window.show()

    def run(self):
        # loop
        while not self.stop_timer:
            # test setup for structure



class TimingWindow(QWidget):
    def __init__(self):

    # GUI for timers

class DefaultThread(QThread):
    # Thread for slideshow

# class DefaultWindow(QWidget):
    # keeping here just in case

# def Main():
app = QApplication([])
caller = MainCaller()
sys.exit(app.exec_())


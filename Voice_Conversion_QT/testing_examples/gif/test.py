from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel(self)
        movie = QMovie('./fish.gif')
        label.setMovie(movie)
        movie.start()
        self.movie = movie

        button = QPushButton("pause/start", self)
        button.clicked.connect(self.pause)
        layout.addWidget(label)
        layout.addWidget(button)
    def pause(self):
        state = self.movie.state()
        state = state != QMovie.Paused
        self.movie.setPaused(state)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import time
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)
        button.clicked.connect(self.xxx)
        layout.addWidget(button, 0, 0)
    def on_button_clicked(self):
        time.sleep(3)   
        print("The button was pressed!")
    def xxx(self):
        print("xxx")
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


#!/usr/bin/env python
import librosa
import librosa.display
import sounddevice as sd
import numpy as np

import display.display as display
import record
import record.record_tools
import record.ui

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton,
                QWidget, QAction, QTabWidget,
                QVBoxLayout, QMessageBox, QHBoxLayout, QGroupBox, QLabel
                ,QWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

import inspect

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class App(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "Voice Conversion App"
    self.left = 0
    self.top = 0
    self.width = 800
    self.height = 800
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    
    self.central_widget = QWidget()
    self.layout = QHBoxLayout(self.central_widget)

    self.speaker_widget = display.SignalDisplayWidget(self, "Speaker")
    self.convert_widget = display.SignalDisplayWidget(self, "Convert")

    self.control_panel  = QGroupBox("Control Panel")
    self.build_control_widget() # will create self.control_widget
   
    self.left_group = QGroupBox("Speaker")
    self.left_group_layout = QHBoxLayout(self.left_group)

    self.left_group_layout.addWidget(self.speaker_widget)
    self.left_group_layout.addWidget(self.control_widget)
    self.layout.addWidget(self.left_group)
    self.layout.addWidget(self.convert_widget)
    
    self.control_items["Load"].clicked.connect(lambda: self.speaker_widget.load_audio())
    self.control_items["Record"].clicked.connect(lambda: self.record_callback())

    self.setCentralWidget(self.central_widget)
    self.show()
    
  def build_control_widget(self):
    self.control_widget = QWidget()
    self.control_layout = QVBoxLayout()
    self.control_items = dict()
    CI = self.control_items
    # Label
    CI["Label"] = QLabel("==Sound==")
    # Push Buttons
    button_names = ["Load", "Record", "Convert"]
    for _name in button_names:
      CI[_name] = QPushButton(_name, self)
    
    for _, item in CI.items():
       self.control_layout.addWidget(item)
    self.control_layout.addStretch(1)
    self.control_widget.setLayout(self.control_layout)
  
  def record_callback(self):
    signal, sr = record.ui.record_dialog()
    self.speaker_widget.set_audio(signal, sr)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())

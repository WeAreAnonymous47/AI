#!/usr/bin/python3
from PyQt5.QtWidgets import QDialog, QApplication
import sys
import os
from AI_Design import *
import time
from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QRect
from pygame import mixer



class FileManager(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AI()
        self.ui.setupUi(self)
        self.show()
        self.Loop()


    def Loop(self):
        self.light = QPropertyAnimation(self.ui.HologramLight, b"geometry")
        self.light.setDirection(1)
        self.light.setLoopCount(2)
        self.light.setStartValue(QRect(0, 781, 481, 20))
        self.light.setEndValue(QRect(0, 340, 481, 461))
        self.light.start()
        self.light.stop()

        self.anim = QPropertyAnimation(self.ui.Blur2, b"geometry")
        self.anim.setDirection(1)
        self.anim.setLoopCount(100)
        self.anim.setStartValue(QRect(110, 240, 231, 231))
        self.anim.setEndValue(QRect(130, 240, 231, 231))
        self.anim.start()

        mixer.init()
        mixer.music.load('/root/PycharmProjects/AI/good.mp3')
        mixer.music.play()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FileManager()
    w.show()
    sys.exit(app.exec_())

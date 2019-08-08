# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AI(object):
    def setupUi(self, AI):
        AI.setObjectName("AI")
        AI.resize(483, 800)
        AI.setWindowTitle("")
        AI.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridLayout_2 = QtWidgets.QGridLayout(AI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.HomePage = QtWidgets.QFrame(AI)
        self.HomePage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HomePage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HomePage.setObjectName("HomePage")
        self.label = QtWidgets.QLabel(self.HomePage)
        self.label.setGeometry(QtCore.QRect(90, 90, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label.setObjectName("label")
        self.Blur2 = QtWidgets.QLabel(self.HomePage)
        self.Blur2.setGeometry(QtCore.QRect(120, 240, 231, 231))
        self.Blur2.setStyleSheet("image: url(/root/PycharmProjects/AI/Hologram Image/Blur 2 Transparent.png);\n"
"background-color: transparent;")
        self.Blur2.setText("")
        self.Blur2.setObjectName("Blur2")
        self.Blur1 = QtWidgets.QLabel(self.HomePage)
        self.Blur1.setGeometry(QtCore.QRect(120, 240, 231, 231))
        self.Blur1.setStyleSheet("image: url(/root/PycharmProjects/AI/Hologram Image/Blur 1 Transparent.png);\n"
"background-color: transparent;")
        self.Blur1.setText("")
        self.Blur1.setObjectName("Blur1")
        self.Original = QtWidgets.QLabel(self.HomePage)
        self.Original.setGeometry(QtCore.QRect(120, 240, 231, 231))
        self.Original.setStyleSheet("image: url(/root/PycharmProjects/AI/Hologram Image/Original Transparent.png);\n"
"background-color: transparent;")
        self.Original.setText("")
        self.Original.setObjectName("Original")
        self.HologramLight = QtWidgets.QLabel(self.HomePage)
        self.HologramLight.setGeometry(QtCore.QRect(0, 760, 471, 31))
        self.HologramLight.setStyleSheet("image: url(/root/PycharmProjects/AI/Hologram Image/Light Transperant.png);\n"
"background-color: transparent;")
        self.HologramLight.setText("")
        self.HologramLight.setObjectName("HologramLight")
        self.gridLayout_2.addWidget(self.HomePage, 0, 0, 1, 1)

        self.retranslateUi(AI)
        QtCore.QMetaObject.connectSlotsByName(AI)

    def retranslateUi(self, AI):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("AI", "How may I help you?"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emgPlotForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_emgPlotForm(object):
    def setupUi(self, emgPlotForm):
        emgPlotForm.setObjectName(_fromUtf8("emgPlotForm"))
        emgPlotForm.resize(1031, 634)
        emgPlotForm.setMinimumSize(QtCore.QSize(1031, 634))
        emgPlotForm.setMaximumSize(QtCore.QSize(1031, 634))
        self.line = QtGui.QFrame(emgPlotForm)
        self.line.setGeometry(QtCore.QRect(0, 70, 1031, 16))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(emgPlotForm)
        self.label.setGeometry(QtCore.QRect(0, 10, 1031, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 91);"))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(emgPlotForm)
        self.line_2.setGeometry(QtCore.QRect(0, 590, 1031, 16))
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(emgPlotForm)
        self.line_3.setGeometry(QtCore.QRect(700, 80, 20, 521))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(emgPlotForm)
        self.line_4.setGeometry(QtCore.QRect(0, 330, 711, 16))
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_7 = QtGui.QFrame(emgPlotForm)
        self.line_7.setGeometry(QtCore.QRect(340, 80, 20, 511))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_5 = QtGui.QFrame(emgPlotForm)
        self.line_5.setGeometry(QtCore.QRect(0, 200, 711, 16))
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(emgPlotForm)
        self.line_6.setGeometry(QtCore.QRect(0, 460, 711, 16))
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_2 = QtGui.QLabel(emgPlotForm)
        self.label_2.setGeometry(QtCore.QRect(720, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_8 = QtGui.QFrame(emgPlotForm)
        self.line_8.setGeometry(QtCore.QRect(710, 430, 321, 20))
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(emgPlotForm)
        self.line_9.setGeometry(QtCore.QRect(710, 510, 321, 20))
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.ch1Label = QtGui.QLabel(emgPlotForm)
        self.ch1Label.setGeometry(QtCore.QRect(10, 80, 341, 121))
        self.ch1Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch1Label.setText(_fromUtf8(""))
        self.ch1Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch1Label.setScaledContents(False)
        self.ch1Label.setObjectName(_fromUtf8("ch1Label"))
        self.ch2Label = QtGui.QLabel(emgPlotForm)
        self.ch2Label.setGeometry(QtCore.QRect(360, 80, 341, 121))
        self.ch2Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch2Label.setText(_fromUtf8(""))
        self.ch2Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch2Label.setObjectName(_fromUtf8("ch2Label"))
        self.ch3Label = QtGui.QLabel(emgPlotForm)
        self.ch3Label.setGeometry(QtCore.QRect(10, 210, 341, 121))
        self.ch3Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch3Label.setText(_fromUtf8(""))
        self.ch3Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch3Label.setObjectName(_fromUtf8("ch3Label"))
        self.ch4Label = QtGui.QLabel(emgPlotForm)
        self.ch4Label.setGeometry(QtCore.QRect(360, 210, 341, 121))
        self.ch4Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch4Label.setText(_fromUtf8(""))
        self.ch4Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch4Label.setObjectName(_fromUtf8("ch4Label"))
        self.ch6Label = QtGui.QLabel(emgPlotForm)
        self.ch6Label.setGeometry(QtCore.QRect(360, 340, 341, 121))
        self.ch6Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch6Label.setText(_fromUtf8(""))
        self.ch6Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch6Label.setObjectName(_fromUtf8("ch6Label"))
        self.ch8Label = QtGui.QLabel(emgPlotForm)
        self.ch8Label.setGeometry(QtCore.QRect(360, 470, 341, 121))
        self.ch8Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)"))
        self.ch8Label.setText(_fromUtf8(""))
        self.ch8Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch8Label.setObjectName(_fromUtf8("ch8Label"))
        self.ch5Label = QtGui.QLabel(emgPlotForm)
        self.ch5Label.setGeometry(QtCore.QRect(10, 340, 341, 121))
        self.ch5Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch5Label.setText(_fromUtf8(""))
        self.ch5Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch5Label.setObjectName(_fromUtf8("ch5Label"))
        self.ch7Label = QtGui.QLabel(emgPlotForm)
        self.ch7Label.setGeometry(QtCore.QRect(10, 470, 341, 121))
        self.ch7Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.ch7Label.setText(_fromUtf8(""))
        self.ch7Label.setPixmap(QtGui.QPixmap(_fromUtf8("src/u=1365459538,710677635&fm=26&gp=0.jpg")))
        self.ch7Label.setObjectName(_fromUtf8("ch7Label"))
        self.layoutWidget = QtGui.QWidget(emgPlotForm)
        self.layoutWidget.setGeometry(QtCore.QRect(720, 140, 291, 251))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ch1CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch1CheckBox.setText(_fromUtf8(""))
        self.ch1CheckBox.setObjectName(_fromUtf8("ch1CheckBox"))
        self.horizontalLayout.addWidget(self.ch1CheckBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.ch2CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch2CheckBox.setText(_fromUtf8(""))
        self.ch2CheckBox.setObjectName(_fromUtf8("ch2CheckBox"))
        self.horizontalLayout_2.addWidget(self.ch2CheckBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.ch3CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch3CheckBox.setText(_fromUtf8(""))
        self.ch3CheckBox.setObjectName(_fromUtf8("ch3CheckBox"))
        self.horizontalLayout_3.addWidget(self.ch3CheckBox)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.ch4CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch4CheckBox.setText(_fromUtf8(""))
        self.ch4CheckBox.setObjectName(_fromUtf8("ch4CheckBox"))
        self.horizontalLayout_4.addWidget(self.ch4CheckBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.ch5CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch5CheckBox.setText(_fromUtf8(""))
        self.ch5CheckBox.setObjectName(_fromUtf8("ch5CheckBox"))
        self.horizontalLayout_5.addWidget(self.ch5CheckBox)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.ch6CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch6CheckBox.setText(_fromUtf8(""))
        self.ch6CheckBox.setObjectName(_fromUtf8("ch6CheckBox"))
        self.horizontalLayout_6.addWidget(self.ch6CheckBox)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.ch7CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch7CheckBox.setText(_fromUtf8(""))
        self.ch7CheckBox.setObjectName(_fromUtf8("ch7CheckBox"))
        self.horizontalLayout_7.addWidget(self.ch7CheckBox)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.ch8CheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ch8CheckBox.setText(_fromUtf8(""))
        self.ch8CheckBox.setObjectName(_fromUtf8("ch8CheckBox"))
        self.horizontalLayout_8.addWidget(self.ch8CheckBox)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem19)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.layoutWidget1 = QtGui.QWidget(emgPlotForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(720, 450, 301, 61))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem20)
        self.startPlotPushBt = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.startPlotPushBt.setFont(font)
        self.startPlotPushBt.setObjectName(_fromUtf8("startPlotPushBt"))
        self.horizontalLayout_13.addWidget(self.startPlotPushBt)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem21)
        self.stopPushBt = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stopPushBt.setFont(font)
        self.stopPushBt.setObjectName(_fromUtf8("stopPushBt"))
        self.horizontalLayout_13.addWidget(self.stopPushBt)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem22)
        self.layoutWidget2 = QtGui.QWidget(emgPlotForm)
        self.layoutWidget2.setGeometry(QtCore.QRect(740, 530, 271, 61))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem23)
        self.saveImagePushBt = QtGui.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.saveImagePushBt.setFont(font)
        self.saveImagePushBt.setObjectName(_fromUtf8("saveImagePushBt"))
        self.horizontalLayout_14.addWidget(self.saveImagePushBt)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem24)
        self.widget = QtGui.QWidget(emgPlotForm)
        self.widget.setGeometry(QtCore.QRect(720, 390, 291, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_11 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_15.addWidget(self.label_11)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem25)
        self.selectAllCheckBox = QtGui.QCheckBox(self.widget)
        self.selectAllCheckBox.setText(_fromUtf8(""))
        self.selectAllCheckBox.setChecked(True)
        self.selectAllCheckBox.setObjectName(_fromUtf8("selectAllCheckBox"))
        self.horizontalLayout_15.addWidget(self.selectAllCheckBox)
        spacerItem26 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem26)
        self.label_12 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_15.addWidget(self.label_12)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem27)
        self.selectNoCheckBox = QtGui.QCheckBox(self.widget)
        self.selectNoCheckBox.setText(_fromUtf8(""))
        self.selectNoCheckBox.setObjectName(_fromUtf8("selectNoCheckBox"))
        self.horizontalLayout_15.addWidget(self.selectNoCheckBox)
        spacerItem28 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem28)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()
        self.label.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_7.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label_2.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.ch1Label.raise_()
        self.ch2Label.raise_()
        self.ch3Label.raise_()
        self.ch4Label.raise_()
        self.ch6Label.raise_()
        self.ch8Label.raise_()
        self.ch5Label.raise_()
        self.ch7Label.raise_()
        self.label_11.raise_()
        self.selectAllCheckBox.raise_()
        self.label_12.raise_()
        self.selectNoCheckBox.raise_()

        self.retranslateUi(emgPlotForm)
        QtCore.QMetaObject.connectSlotsByName(emgPlotForm)

    def retranslateUi(self, emgPlotForm):
        emgPlotForm.setWindowTitle(_translate("emgPlotForm", "emgPlotForm", None))
        self.label.setText(_translate("emgPlotForm", "表面肌电信号波形显示", None))
        self.label_2.setText(_translate("emgPlotForm", "通道选择：", None))
        self.label_3.setText(_translate("emgPlotForm", "ch1：", None))
        self.label_4.setText(_translate("emgPlotForm", "ch2：", None))
        self.label_5.setText(_translate("emgPlotForm", "ch3：", None))
        self.label_6.setText(_translate("emgPlotForm", "ch4：", None))
        self.label_7.setText(_translate("emgPlotForm", "ch5：", None))
        self.label_10.setText(_translate("emgPlotForm", "ch6：", None))
        self.label_9.setText(_translate("emgPlotForm", "ch7：", None))
        self.label_8.setText(_translate("emgPlotForm", "ch8：", None))
        self.startPlotPushBt.setText(_translate("emgPlotForm", "开始", None))
        self.stopPushBt.setText(_translate("emgPlotForm", "结束", None))
        self.saveImagePushBt.setText(_translate("emgPlotForm", "保存", None))
        self.label_11.setText(_translate("emgPlotForm", "全选：", None))
        self.label_12.setText(_translate("emgPlotForm", "全不选：", None))


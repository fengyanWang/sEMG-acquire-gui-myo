# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveFileForm.ui'
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

class Ui_saveFileForm(object):
    def setupUi(self, saveFileForm):
        saveFileForm.setObjectName(_fromUtf8("saveFileForm"))
        saveFileForm.resize(403, 330)
        saveFileForm.setMinimumSize(QtCore.QSize(403, 330))
        saveFileForm.setMaximumSize(QtCore.QSize(403, 330))
        self.widget = QtGui.QWidget(saveFileForm)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.fileNameLineEdit = QtGui.QLineEdit(self.widget)
        self.fileNameLineEdit.setObjectName(_fromUtf8("fileNameLineEdit"))
        self.horizontalLayout.addWidget(self.fileNameLineEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.fileTypeComboBox = QtGui.QComboBox(self.widget)
        self.fileTypeComboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.fileTypeComboBox.setObjectName(_fromUtf8("fileTypeComboBox"))
        self.fileTypeComboBox.addItem(_fromUtf8(""))
        self.fileTypeComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.fileTypeComboBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtGui.QWidget(saveFileForm)
        self.widget1.setGeometry(QtCore.QRect(10, 220, 381, 101))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.saveFIlePlotPushBt = QtGui.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.saveFIlePlotPushBt.setFont(font)
        self.saveFIlePlotPushBt.setObjectName(_fromUtf8("saveFIlePlotPushBt"))
        self.horizontalLayout_3.addWidget(self.saveFIlePlotPushBt)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.canclePushBt = QtGui.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.canclePushBt.setFont(font)
        self.canclePushBt.setObjectName(_fromUtf8("canclePushBt"))
        self.horizontalLayout_3.addWidget(self.canclePushBt)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)

        self.retranslateUi(saveFileForm)
        QtCore.QMetaObject.connectSlotsByName(saveFileForm)

    def retranslateUi(self, saveFileForm):
        saveFileForm.setWindowTitle(_translate("saveFileForm", "saveFileForm", None))
        self.label_2.setText(_translate("saveFileForm", "文件名：", None))
        self.label_3.setText(_translate("saveFileForm", "文件格式：", None))
        self.fileTypeComboBox.setItemText(0, _translate("saveFileForm", "csv", None))
        self.fileTypeComboBox.setItemText(1, _translate("saveFileForm", "txt", None))
        self.saveFIlePlotPushBt.setText(_translate("saveFileForm", "保存", None))
        self.canclePushBt.setText(_translate("saveFileForm", "取消", None))


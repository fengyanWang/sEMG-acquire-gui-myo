#coding:UTF-8

import sys
from PyQt4 import QtCore, QtGui
from dataAcquireWin import Ui_dataAcquireWin
from emgPlotForm import Ui_emgPlotForm
from saveFileForm import Ui_saveFileForm

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        # build ui
        self.ui = Ui_saveFileForm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
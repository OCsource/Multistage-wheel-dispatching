# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# @author   : 关宅宅
# @time     : 2019-2-19 19:53
# @file     : mainUI.py
# @Software : PyCharm Community Edition

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import UI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
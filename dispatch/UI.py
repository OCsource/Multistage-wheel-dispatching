# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import multiply,process
import time,random

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

NUM = 1

#创建一个matplotlib图形绘制类
class MyCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # self.axes.clear()
        # self.axes.set_aspect('auto')
        # We want the axes cleared every time plot() is called
        # self.axes.cla()

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, self.fig)
        # self.setParent(parent)

    def compute_initial_figure(self):
        pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 460)
        self.time = time.time()
        self.started = False
        self.x = [0]
        self.y = [1]

        # 布局
        self.canvas = MyCanvas(self, width=5, height=4, dpi=100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 小部件布局
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 60, 20))
        self.label.setObjectName("label")
        self.QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit.setGeometry(QtCore.QRect(260, 50, 140, 18))
        self.QLineEdit.setObjectName("QLineEdit")
        self.QLineEdit.setReadOnly(True)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(260, 90, 60, 20))
        self.label_1.setObjectName("label_1")
        self.QLineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit_1.setGeometry(QtCore.QRect(260, 120, 140, 18))
        self.QLineEdit_1.setObjectName("QLineEdit_1")
        self.QLineEdit_1.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 165, 60, 20))
        self.label_2.setObjectName("label_2")
        self.QLineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit_2.setGeometry(QtCore.QRect(260, 195, 140, 18))
        self.QLineEdit_2.setObjectName("QLineEdit_2")
        self.QLineEdit_2.setReadOnly(True)

        # 大部件布局
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 220, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem("%2s%13s%15s"%('编号','进入时间','服务时间'))
        self.textList = QtWidgets.QTextEdit(self.centralwidget)
        self.textList.setGeometry(QtCore.QRect(10, 230, 400, 200))
        self.textList.setObjectName("textList")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 20, 550, 420))
        self.groupBox.setObjectName("groupBox")
        # self.textList.setStyleSheet("background-color:black")
        # self.textList.setTextColor(QtGui.QColor(255, 255, 255))
        self.textList.setReadOnly(True)
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.canvas)

        # 多余布局
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(330, 370, 75, 23))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton0.setGeometry(QtCore.QRect(420, 370, 75, 23))
        # self.pushButton0.setObjectName("pushButton0")
        # self.pushButton.setVisible(False)
        # self.pushButton0.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 事件
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #参数QtCore.Qt.CustomContextMenu
        self.contextMenu = QtWidgets.QMenu()
        self.outContextMenu = QtWidgets.QMenu()
        self.actionIns = self.outContextMenu.addAction(QtGui.QIcon("./resource/+.png"), u'|  添加')
        self.listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.showMenu)
        self.actionIns.triggered.connect(self.insertItem)

        self.line, = self.canvas.axes.plot(self.x, self.y, animated=True, lw=2)
        # self.canvas.axes.set_xlim([0, 100])
        # self.canvas.axes.set_ylim([0, 10])
        self.canvas.axes.set_xbound(0,100)
        self.canvas.axes.set_ybound(0,10)
        # self.canvas.axes.set_xlabel(u'时间')
        # self.canvas.axes.set_ylabel(u'线程id')
        # self.pushButton.clicked.connect(self.on_start)
        # self.pushButton0.clicked.connect(self.on_stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "多级轮转抢占式"))
        # self.pushButton.setText(_translate("MainWindow", "开始"))
        # self.pushButton0.setText(_translate("MainWindow", "暂停"))
        self.label.setText(_translate("MainWindow", "队列一："))
        self.label_1.setText(_translate("MainWindow", "队列二："))
        self.label_2.setText(_translate("MainWindow", "队列三："))

    # 添加方法
    def insertItem(self):
        self.getText()
        global NUM
        NUM += 1

    # 输入对话框
    def getText(self):
        server, okPressed = QtWidgets.QInputDialog.getText(self.centralwidget, "服务时间", "请输入该线程的服务时间：", QtWidgets.QLineEdit.Normal, "")
        if okPressed and server.isdigit():
            if self.listWidget.count() == 1:
                # self.pushButton.setVisible(True)
                # self.pushButton0.setVisible(True)
                global startTime
                startTime = time.time()
                first = NUM
                second = int(time.time() - startTime)
                thrid = int(server)
                Process = process.process(NUM, second, int(server))
                # 线程处理数据
                self.apply = multiply.applyRound(True, 0,self)
                self.apply.dictP[NUM] = Process
                self.apply.start()
                # 启动画图
                self.on_start()
            else:
                first = NUM
                second = self.apply.allTime
                thrid = int(server)
                print('新的线程加入队列...')
                Process = process.process(NUM, second, int(server))
                self.apply.hasSomeProcessCome = True
                self.apply.dictP[NUM] = Process
            s = (f'  {str(first)}\t{str(second)}\t {str(thrid)}')
            self.listWidget.addItem(s)

    # 显示列表菜单
    def showMenu(self,point):
        item = self.listWidget.itemAt(point)
        if item:
            pass
        else:
            self.outContextMenu.show()
            self.outContextMenu.exec_(QtGui.QCursor.pos())

    # 暂停
    def stopThread(self):
        pass

    # 开始
    def awaitThread(self):
        pass

    # 以下均为画图
    # 更新
    def update_line(self, i):
        # i = time.time() - self.time
        # self.canvas.axes.cla()
        # self.x.append(i)
        # self.y.append(i * random.randint(0, 2))
        # print(self.x)
        # print(self.y)

        # 更新方法一
        # self.canvas.axes.set_xlim([0, max(self.x) + 1])
        # self.canvas.axes.set_ylim([0, max(self.y) + 1])
        # self.canvas.axes.update_datalim([[0, max(self.x) + 1],[0, max(self.y) + 1]])

        # 更新方法二
        # self.canvas.axes.cla()
        # self.canvas.axes.set_xbound(0, max(self.x) + 1)
        # self.canvas.axes.set_ybound(0, max(self.y) + 1)

        # 更新方法三
        # self.canvas.axes.set_xticks([0, max(self.x) + 1])
        # self.canvas.axes.set_yticks([0, max(self.y) + 1])
        # self.canvas.axes.set_axis_on()

        # 以上方法都没有什么用

        self.line.set_xdata(self.x)
        self.line.set_ydata(self.y)
        return [self.line]

    # 开始暂停（开始）
    def on_start(self):
        if self.started:
            pass
        else:
            self.ani = FuncAnimation(self.canvas.figure, self.update_line,
                                 blit=True, interval=1050)
            self.started = True

    # 开始暂停（暂停）
    def on_stop(self):
        if self.started:
            self.ani._stop()
            self.started = False
        else:
            self.ani._stop()

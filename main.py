from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MagicMirror(object):
    def setupUi(self, MagicMirror):
        MagicMirror.setObjectName("MagicMirror")
        MagicMirror.setGeometry(60, 60, 1800, 950)
        self.centralwidget = QtWidgets.QWidget(MagicMirror)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 0, 1770, 920))
        self.frame.setStyleSheet("border-image: url(:/);")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(60, 40, 1681, 841))
        self.background.setStyleSheet(
            "border-image: url(:/resources/background.jpg));")
        self.background.setText("")
        self.background.setObjectName("background")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(860, 100, 631, 701))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.time_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.time_3.setStyleSheet("color: rgb(134, 15, 4);\n"
                                  "font: 65pt \"Forte\";")
        self.time_3.setAlignment(QtCore.Qt.AlignCenter)
        self.time_3.setObjectName("time_3")
        self.verticalLayout.addWidget(self.time_3)
        self.news1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news1.setStyleSheet("color: rgb(3, 37, 67);\n"
                                 "font: 24pt \"Forte\";")
        self.news1.setAlignment(QtCore.Qt.AlignCenter)
        self.news1.setObjectName("news1")
        self.verticalLayout.addWidget(self.news1)
        self.news2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news2.setStyleSheet("color: rgb(3, 37, 67);\n"
                                 "font: 24pt \"Forte\";")
        self.news2.setAlignment(QtCore.Qt.AlignCenter)
        self.news2.setObjectName("news2")
        self.verticalLayout.addWidget(self.news2)
        self.news3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news3.setStyleSheet("color: rgb(3, 37, 67);\n"
                                 "font: 24pt \"Forte\";")
        self.news3.setAlignment(QtCore.Qt.AlignCenter)
        self.news3.setObjectName("news3")
        self.verticalLayout.addWidget(self.news3)
        self.news4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news4.setStyleSheet("color: rgb(3, 37, 67);\n"
                                 "font: 24pt \"Forte\";")
        self.news4.setAlignment(QtCore.Qt.AlignCenter)
        self.news4.setObjectName("news4")
        self.verticalLayout.addWidget(self.news4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(200, 160, 591, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.time = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
                                "font: 65pt \"Forte\";")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.verticalLayout_2.addWidget(self.time)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.year.setStyleSheet("color: rgb(162, 255, 237);\n"
                                "font: 24pt \"Forte\";")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.month = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.month.setStyleSheet("color: rgb(162, 255, 237);\n"
                                 "font: 24pt \"Forte\";")
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.day = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.day.setStyleSheet("color: rgb(162, 255, 237);\n"
                               "font: 24pt \"Forte\";")
        self.day.setAlignment(QtCore.Qt.AlignCenter)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.time_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_2.setStyleSheet("color: rgb(113, 51, 157);\n"
                                  "font: 65pt \"Forte\";")
        self.time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_2.setObjectName("time_2")
        self.verticalLayout_2.addWidget(self.time_2)
        self.weather = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.weather.setStyleSheet("color: rgb(133, 255, 247);\n"
                                   "font: 30pt \"Forte\";")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        self.verticalLayout_2.addWidget(self.weather)
        self.background.raise_()
        self.frame.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        MagicMirror.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MagicMirror)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 26))
        self.menubar.setObjectName("menubar")
        MagicMirror.setMenuBar(self.menubar)

        self.retranslateUi(MagicMirror)
        QtCore.QMetaObject.connectSlotsByName(MagicMirror)

    def retranslateUi(self, MagicMirror):
        _translate = QtCore.QCoreApplication.translate
        MagicMirror.setWindowTitle(_translate("MagicMirror", "MainWindow"))
        self.time_3.setText(_translate("MagicMirror", "news"))
        self.news1.setText(_translate(
            "MagicMirror", "news 1 is gonna be here and it is int"))
        self.news2.setText(_translate(
            "MagicMirror", "news 1 is gonna be here and it is int"))
        self.news3.setText(_translate(
            "MagicMirror", "news 1 is gonna be here and it is int"))
        self.news4.setText(_translate(
            "MagicMirror", "news 1 is gonna be here and it is int"))
        self.time.setText(_translate("MagicMirror", "22:22"))
        self.year.setText(_translate("MagicMirror", "2000"))
        self.month.setText(_translate("MagicMirror", "Month"))
        self.day.setText(_translate("MagicMirror", "00"))
        self.time_2.setText(_translate("MagicMirror", "22*"))
        self.weather.setText(_translate(
            "MagicMirror", "Tehran weather is here"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MagicMirror = QtWidgets.QMainWindow()
    ui = Ui_MagicMirror()
    ui.setupUi(MagicMirror)
    MagicMirror.show()
    sys.exit(app.exec_())

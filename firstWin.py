from multiprocessing.connection import wait
from turtle import update
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import pyttsx3
from bs4 import BeautifulSoup
from gnews import GNews
import requests
import cv2
import pytz
import sys
import pics
import jdatetime
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os
import time
import main

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


class Ui_MagicMirror(QMainWindow):
    def setupUi(self, MagicMirror):
        MagicMirror.setObjectName("MagicMirror")
        MagicMirror.setGeometry(60 , 60 , 1800, 950)
        self.centralwidget = QtWidgets.QWidget(MagicMirror)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 0, 1770, 920))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/frame.png);")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(60, 40, 1681, 841))
        self.background.setStyleSheet("border-image: url(:/newPrefix/background.jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(920, 70, 631, 701))
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
        self.news1.setWordWrap(True)
        self.verticalLayout.addWidget(self.news1)
        self.news2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news2.setStyleSheet("color: rgb(3, 37, 67);\n"
"font: 24pt \"Forte\";")
        self.news2.setAlignment(QtCore.Qt.AlignCenter)
        self.news2.setObjectName("news2")
        self.news2.setWordWrap(True)
        self.verticalLayout.addWidget(self.news2)
        self.news3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news3.setStyleSheet("color: rgb(3, 37, 67);\n"
"font: 24pt \"Forte\";")
        self.news3.setAlignment(QtCore.Qt.AlignCenter)
        self.news3.setObjectName("news3")
        self.news3.setWordWrap(True)
        self.verticalLayout.addWidget(self.news3)
        self.news4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news4.setStyleSheet("color: rgb(3, 37, 67);\n"
"font: 24pt \"Forte\";")
        self.news4.setAlignment(QtCore.Qt.AlignCenter)
        self.news4.setObjectName("news4")
        self.news4.setWordWrap(True)
        self.verticalLayout.addWidget(self.news4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 60, 211, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.clicked(1))
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(150, 160, 589, 135))
        self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
"font: 65pt \"Forte\";")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 250, 589, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLabel(self.layoutWidget)
        self.year.setStyleSheet("color: rgb(162, 255, 237);\n"
"font: 24pt \"Forte\";")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.month = QtWidgets.QLabel(self.layoutWidget)
        self.month.setStyleSheet("color: rgb(162, 255, 237);\n"
"font: 24pt \"Forte\";")
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.day = QtWidgets.QLabel(self.layoutWidget)
        self.day.setStyleSheet("color: rgb(162, 255, 237);\n"
"font: 24pt \"Forte\";")
        self.day.setAlignment(QtCore.Qt.AlignCenter)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.time_2 = QtWidgets.QLabel(self.centralwidget)
        self.time_2.setGeometry(QtCore.QRect(120, 320, 589, 276))
        self.time_2.setStyleSheet("color: rgb(113, 51, 157);\n"
"font: 65pt \"Forte\";")
        self.time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_2.setObjectName("time_2")
        self.weather = QtWidgets.QLabel(self.centralwidget)
        self.weather.setGeometry(QtCore.QRect(130, 480, 641, 171))
        self.weather.setStyleSheet("color: rgb(133, 255, 247);\n"
"font: 30pt \"Forte\";")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        self.weather.setWordWrap(True)
        self.timeIcon = QtWidgets.QLabel(self.centralwidget)
        self.timeIcon.setGeometry(QtCore.QRect(700, 180, 91, 91))
        self.timeIcon.setStyleSheet("border-image: url(:/newPrefix/time.png);")
        self.timeIcon.setText("")
        self.timeIcon.setObjectName("timeIcon")
        self.dateIcon = QtWidgets.QLabel(self.centralwidget)
        self.dateIcon.setGeometry(QtCore.QRect(710, 290, 71, 81))
        self.dateIcon.setStyleSheet("border-image: url(:/newPrefix/calender.png);")
        self.dateIcon.setText("")
        self.dateIcon.setObjectName("dateIcon")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(520, 410, 91, 91))
        self.temp.setStyleSheet("border-image: url(:/newPrefix/temp.png);")
        self.temp.setText("")
        self.temp.setObjectName("temp")
        self.weatherIcon = QtWidgets.QLabel(self.centralwidget)
        self.weatherIcon.setGeometry(QtCore.QRect(720, 500, 111, 101))
        self.weatherIcon.setStyleSheet("border-image: url(:/newPrefix/weather.png);")
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")
        self.background.raise_()
        self.frame.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.time.raise_()
        self.layoutWidget.raise_()
        self.time_2.raise_()
        self.weather.raise_()
        self.timeIcon.raise_()
        self.dateIcon.raise_()
        self.temp.raise_()
        self.weatherIcon.raise_()
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
        #self.initNews()
        self.initDate()
        self.initWeather()
        self.updateTemperature()
        self.updateTimezone()

    def initNews(self):
        _translate = QtCore.QCoreApplication.translate
        iran_news = GNews().get_news_by_topic("Technology")
        self.news1.setText(_translate(
            "MagicMirror", iran_news[0].get("title")))
        self.news2.setText(_translate(
            "MagicMirror", iran_news[1].get("title")))
        self.news3.setText(_translate(
            "MagicMirror", iran_news[2].get("title")))
        self.news4.setText(_translate(
            "MagicMirror", iran_news[3].get("title")))

    def updateTimezone(self):
        _translate = QtCore.QCoreApplication.translate
        now = datetime.now()
        time_str = str(now.hour) + " : " + \
            str(now.minute) + " : " + str(now.second)
        self.time.setText(_translate("MagicMirror", time_str))

    def initDate(self):
        now = datetime.now()
        _translate = QtCore.QCoreApplication.translate
        months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad",
                  "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]
        jalili_date = jdatetime.date.fromgregorian(
            day=now.day, month=now.month, year=now.year)
        self.year.setText(_translate("MagicMirror", str(jalili_date.year)))
        self.month.setText(_translate(
            "MagicMirror", months[jalili_date.month-1]))
        self.day.setText(_translate("MagicMirror", str(jalili_date.day)))

    def initWeather(self):
        _translate = QtCore.QCoreApplication.translate
        city = "Tehran+weather"
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        info = soup.select('#wob_dc')[0].getText().strip()
        self.weather.setText(_translate(
            "MagicMirror", "Tehran weather is \"" + info + "\" today"))

    def updateTemperature(self):
        _translate = QtCore.QCoreApplication.translate
        self.time_2.setText(_translate("MagicMirror", "22°"))

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()
        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda error_msg, error,
                                   msg: self.alert(msg))
        self.capture.imageCaptured.connect(lambda d,
                                           i: self.status.showMessage("Image captured : " 
                                                                      + str(self.save_seq)))
        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0


    def cameraInit(self):
        self.available_cameras = QCameraInfo.availableCameras()           
        self.viewfinder = QCameraViewfinder(self.centralwidget)
        self.viewfinder.show()
        self.viewfinder.setGeometry(60 ,  40 , int(1920 * 3/4 + 60), int(1080 * 3/4 + 40))
        self.select_camera(0)
        

    def clicked (self , num):
    
        if(num == 1):
            self.background.setVisible(False)
            self.verticalLayoutWidget.setVisible(False)
            self.weatherIcon.setVisible(False)
            self.timeIcon.setVisible(False)
            self.temp.setVisible(False)
            self.dateIcon.setVisible(False)
            self.layoutWidget.setGeometry(QtCore.QRect(780, 890, 371, 61))
            self.time_2.setGeometry(QtCore.QRect(1100, 890, 321, 61))
            self.time_2.setStyleSheet("color: rgb(113, 51, 157);\n"
            "font: 30pt \"Forte\";")
            self.time.setGeometry(QtCore.QRect(470, 880, 341, 81))
            self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
            "font: 30pt \"Forte\";")
            self.weather.setVisible(False)
            self.cameraInit()
            

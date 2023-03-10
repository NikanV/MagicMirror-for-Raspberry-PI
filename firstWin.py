from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup
import requests
import cv2
import jdatetime
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import poplib
from email import parser
import numpy as np
from threading import *
import time
import pics, pics2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


class Ui_MagicMirror(QMainWindow):
    def setupUi(self, MagicMirror):
        # Window attributes
        MagicMirror.setObjectName("MagicMirror")
        MagicMirror.setGeometry(60, 60, 1800, 950)
        self.centralWidget = QtWidgets.QWidget(MagicMirror)
        self.centralWidget.setObjectName("centralWidget")

        # Background and frame attributes
        self.frame = QtWidgets.QLabel(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(15, 0, 1770, 920))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/frame.png);")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.centralWidget)
        self.background.setGeometry(QtCore.QRect(60, 40, 1681, 841))
        self.background.setStyleSheet(
            "border-image: url(:/newPrefix/background.jpg);"
            "border-top-left-radius :50px;"
            "border-top-right-radius : 50px; "
            "border-bottom-left-radius : 50px; "
            "border-bottom-right-radius : 50px")
        self.background.setText("")
        self.background.setObjectName("background")

        # The vertical layout for news attributes
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(920, 70, 631, 701))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # News title and descriptions attributes
        self.news = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.news.setStyleSheet("color: rgb(134, 15, 4);\n"
                                "font: 65pt \"Forte\";")
        self.news.setAlignment(QtCore.Qt.AlignCenter)
        self.news.setObjectName("news")
        self.verticalLayout.addWidget(self.news)
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

        # Testing button for user recognition attributes
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 0, 150, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(
            lambda: self.clicked(self.weatherIcon.isVisible()))

        # Time attributes
        self.time = QtWidgets.QLabel(self.centralWidget)
        self.time.setGeometry(QtCore.QRect(150, 160, 589, 135))
        self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
                                "font: 65pt \"Forte\";")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")

        # The horizontal layout for date attributes
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(130, 250, 589, 182))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Date attributes
        self.year = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.year.setStyleSheet("color: rgb(162, 255, 237);\n"
                                "font: 24pt \"Forte\";")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.month = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.month.setStyleSheet("color: rgb(162, 255, 237);\n"
                                 "font: 24pt \"Forte\";")
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.day = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.day.setStyleSheet("color: rgb(162, 255, 237);\n"
                               "font: 24pt \"Forte\";")
        self.day.setAlignment(QtCore.Qt.AlignCenter)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)

        # Temperature attributes
        self.temperature = QtWidgets.QLabel(self.centralWidget)
        self.temperature.setGeometry(QtCore.QRect(120, 320, 589, 276))
        self.temperature.setStyleSheet("color: rgb(113, 51, 157);\n"
                                       "font: 65pt \"Forte\";")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")

        # Weather attributes
        self.weather = QtWidgets.QLabel(self.centralWidget)
        self.weather.setGeometry(QtCore.QRect(130, 480, 641, 171))
        self.weather.setStyleSheet("color: rgb(133, 255, 247);\n"
                                   "font: 30pt \"Forte\";")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        self.weather.setWordWrap(True)

        # Image attributes
        self.image = QtWidgets.QLabel(self.centralWidget)
        self.image.setGeometry(QtCore.QRect(660, 40, 600, 841))
        # self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")

        # Email background attributes
        self.emailBack = QtWidgets.QLabel(self.centralWidget)
        self.emailBack.setGeometry(QtCore.QRect(60, 40, 600, 841))
        self.emailBack.setStyleSheet(
            "border-image: url(:/newPrefix/emailBackground.jpg);"
            "border-top-left-radius :50px;"
            "border-top-right-radius : 5px; "
            "border-bottom-left-radius : 50px; "
            "border-bottom-right-radius : 5px")
        self.emailBack.setText("")
        self.emailBack.setObjectName("emailBack")
        self.emailBack.setVisible(False)

        # The vertical layout for email attributes
        self.verticalLayoutWidget3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget3.setGeometry(
            QtCore.QRect(150, 140, 450, 601))
        self.verticalLayoutWidget3.setObjectName("verticalLayoutWidget3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget3)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayout")

        # Email title and descriptions attributes
        self.emailTitle = QtWidgets.QLabel(self.verticalLayoutWidget3)
        self.emailTitle.setStyleSheet("color: rgb(134, 15, 4);\n"
                                      "font: 30pt \"Forte\";")
        self.emailTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.emailTitle.setObjectName("emailTitle")
        self.verticalLayout3.addWidget(self.emailTitle)
        self.email1 = QtWidgets.QLabel(self.verticalLayoutWidget3)
        self.email1.setStyleSheet("color: rgb(3, 37, 67);\n"
                                  "font: 20pt \"Forte\";")
        self.email1.setAlignment(QtCore.Qt.AlignCenter)
        self.email1.setObjectName("email1")
        self.email1.setWordWrap(True)
        self.verticalLayout3.addWidget(self.email1)
        self.email2 = QtWidgets.QLabel(self.verticalLayoutWidget3)
        self.email2.setStyleSheet("color: rgb(3, 37, 67);\n"
                                  "font: 20pt \"Forte\";")
        self.email2.setAlignment(QtCore.Qt.AlignCenter)
        self.email2.setObjectName("email2")
        self.email2.setWordWrap(True)
        self.verticalLayout3.addWidget(self.email2)
        self.email3 = QtWidgets.QLabel(self.verticalLayoutWidget3)
        self.email3.setStyleSheet("color: rgb(3, 37, 67);\n"
                                  "font: 20pt \"Forte\";")
        self.email3.setAlignment(QtCore.Qt.AlignCenter)
        self.email3.setObjectName("email3")
        self.email3.setWordWrap(True)
        self.verticalLayout3.addWidget(self.email3)
        self.email4 = QtWidgets.QLabel(self.verticalLayoutWidget3)
        self.email4.setStyleSheet("color: rgb(3, 37, 67);\n"
                                  "font: 20pt \"Forte\";")
        self.email4.setAlignment(QtCore.Qt.AlignCenter)
        self.email4.setObjectName("email4")
        self.email4.setWordWrap(True)
        self.verticalLayout3.addWidget(self.email4)

        # All of the icons attributes
        self.timeIcon = QtWidgets.QLabel(self.centralWidget)
        self.timeIcon.setGeometry(QtCore.QRect(700, 180, 91, 91))
        self.timeIcon.setStyleSheet("border-image: url(:/newPrefix/time.png);")
        self.timeIcon.setText("")
        self.timeIcon.setObjectName("timeIcon")
        self.dateIcon = QtWidgets.QLabel(self.centralWidget)
        self.dateIcon.setGeometry(QtCore.QRect(710, 290, 71, 81))
        self.dateIcon.setStyleSheet(
            "border-image: url(:/newPrefix/calender.png);")
        self.dateIcon.setText("")
        self.dateIcon.setObjectName("dateIcon")
        self.temperatureIcon = QtWidgets.QLabel(self.centralWidget)
        self.temperatureIcon.setGeometry(QtCore.QRect(520, 410, 91, 91))
        self.temperatureIcon.setStyleSheet(
            "border-image: url(:/newPrefix/temp.png);")
        self.temperatureIcon.setText("")
        self.temperatureIcon.setObjectName("temperatureIcon")
        self.weatherIcon = QtWidgets.QLabel(self.centralWidget)
        self.weatherIcon.setGeometry(QtCore.QRect(720, 500, 111, 101))
        self.weatherIcon.setStyleSheet(
            "border-image: url(:/newPrefix/weather.png);")
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")

        # Raising each widget to be sure that they are all visible
        self.background.raise_()
        self.frame.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.time.raise_()
        self.horizontalLayoutWidget.raise_()
        self.temperature.raise_()
        self.weather.raise_()
        self.timeIcon.raise_()
        self.dateIcon.raise_()
        self.temperatureIcon.raise_()
        self.weatherIcon.raise_()
        self.image.raise_()

        # Initiating the widgets' values
        MagicMirror.setCentralWidget(self.centralWidget)
        self.retranslateUi(MagicMirror)
        QtCore.QMetaObject.connectSlotsByName(MagicMirror)

    def retranslateUi(self, MagicMirror):
        _translate = QtCore.QCoreApplication.translate
        MagicMirror.setWindowTitle(_translate("MagicMirror", "MainWindow"))
        self.news.setText(_translate("MagicMirror", "news"))

        self.initNews(_translate)
        self.initDate(_translate)
        self.initWeather(_translate)
        self.updateTemperature(_translate)
        self.updateTimezone(_translate)
        self.initEmails(_translate)

        self.timeZoneTimer = QTimer()
        self.timeZoneTimer.setInterval(1000)
        self.timeZoneTimer.timeout.connect(self.updateTimezoneAndTemperature)
        self.timeZoneTimer.start()
        self.cameraTimer = QTimer()
        self.cameraTimer.setInterval(10)
        self.cameraTimer.timeout.connect(self.initCamera)

    def updateTimezoneAndTemperature(self):
        _translate = QtCore.QCoreApplication.translate
        self.updateTimezone(_translate)
        self.updateTemperature(_translate)

    def initNews(self, _translate):
        query_params = {
            "source": "bbc-news",
            "sortBy": "top",
            "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
        }
        main_url = " https://newsapi.org/v1/articles"

        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        iran_news = open_bbc_page["articles"]

        if len(iran_news) >= 1:
            self.news1.setText(_translate(
                "MagicMirror", iran_news[0].get("title")))
        if len(iran_news) >= 2:
            self.news2.setText(_translate(
                "MagicMirror", iran_news[1].get("title")))
        if len(iran_news) >= 3:
            self.news3.setText(_translate(
                "MagicMirror", iran_news[2].get("title")))
        if len(iran_news) >= 4:
            self.news4.setText(_translate(
                "MagicMirror", iran_news[3].get("title")))

    def updateTimezone(self, _translate):
        now = datetime.now()
        time_str = str(now.hour) + " : " + \
            str(now.minute) + " : " + str(now.second)
        self.time.setText(_translate("MagicMirror", time_str))

    def initDate(self, _translate):
        now = datetime.now()
        months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad",
                  "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]
        jalili_date = jdatetime.date.fromgregorian(
            day=now.day, month=now.month, year=now.year)
        self.year.setText(_translate("MagicMirror", str(jalili_date.year)))
        self.month.setText(_translate(
            "MagicMirror", months[jalili_date.month-1]))
        self.day.setText(_translate("MagicMirror", str(jalili_date.day)))

    def initWeather(self, _translate):
        res = requests.get(
            'https://www.google.com/search?q=Tehran+weather&oq=Tehran+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        info = soup.select('#wob_dc')[0].getText().strip()
        self.weather.setText(_translate(
            "MagicMirror", "Tehran weather is \"" + info + "\" today"))

    def updateTemperature(self, _translate):
        self.temperature.setText(_translate("MagicMirror", "22??"))

    def initCamera(self):
        url = "http://192.168.0.155:8080/photo.jpg"
        img_response = requests.get(url)
        img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
        cv_image = cv2.imdecode(img_array, -1)
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(1800, 950, Qt.KeepAspectRatio)
        qt_image = QPixmap.fromImage(p)
        self.image.setPixmap(qt_image)

    def initEmails(self, _translate):
        pop3server = 'mail.sharif.edu'
        pop3server = poplib.POP3_SSL(pop3server)
        pop3server.user('ehsan.rahmanimiyab@sharif.edu')
        pop3server.pass_('10878296Ehsan')
        messages = [pop3server.retr(i) for i in range(
            1, len(pop3server.list()[1]) + 1)]
        messages = ['\n'.join(map(bytes.decode, msg[1])) for msg in messages]
        messages = [parser.Parser().parsestr(msg) for msg in messages]
        self.emailTitle.setText(_translate("MagicMirror", "Emails: (Nima)"))
        self.email1.setText(_translate(
            "MagicMirror", messages[0]["subject"] + " - " + messages[0]["from"]))
        self.email2.setText(_translate(
            "MagicMirror", messages[1]["subject"] + " - " + messages[1]["from"]))
        self.email3.setText(_translate(
            "MagicMirror", messages[2]["subject"] + " - " + messages[2]["from"]))
        self.email4.setText(_translate(
            "MagicMirror", messages[3]["subject"] + " - " + messages[3]["from"]))
        pop3server.quit()


    def clicked(self, condition):
        self.background.setVisible(not condition)
        self.verticalLayoutWidget.setVisible(not condition)
        self.weatherIcon.setVisible(not condition)
        self.timeIcon.setVisible(not condition)
        self.temperatureIcon.setVisible(not condition)
        self.dateIcon.setVisible(not condition)
        self.weather.setVisible(not condition)
        self.image.setVisible(condition)
        self.emailBack.setVisible(condition)
        self.verticalLayoutWidget3.setVisible(condition)
        if (condition):
            self.horizontalLayoutWidget.setGeometry(
                QtCore.QRect(780, 890, 371, 61))
            self.temperature.setGeometry(QtCore.QRect(1100, 890, 321, 61))
            self.temperature.setStyleSheet("color: rgb(113, 51, 157);\n"
                                           "font: 30pt \"Forte\";")
            self.time.setGeometry(QtCore.QRect(470, 880, 341, 81))
            self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
                                    "font: 30pt \"Forte\";")
            # self.cameraTimer.start()
        else:
            self.horizontalLayoutWidget.setGeometry(
                QtCore.QRect(130, 250, 589, 182))
            self.temperature.setGeometry(QtCore.QRect(120, 320, 589, 276))
            self.temperature.setStyleSheet("color: rgb(113, 51, 157);\n"
                                           "font: 65pt \"Forte\";")
            self.time.setGeometry(QtCore.QRect(150, 160, 589, 135))
            self.time.setStyleSheet("color: rgb(113, 51, 157);\n"
                                    "font: 65pt \"Forte\";")
            # self.cameraTimer.stop()

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
import firstWin


app = QtWidgets.QApplication(sys.argv)


def changeWindow(MagicMirror):
    ui = firstWin.Ui_MagicMirror()
    ui.setupUi(MagicMirror)
    MagicMirror.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    MagicMirror = QtWidgets.QMainWindow()
    changeWindow(MagicMirror)

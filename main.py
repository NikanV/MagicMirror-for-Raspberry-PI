from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
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

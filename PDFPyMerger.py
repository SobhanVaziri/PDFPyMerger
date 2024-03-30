from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType, loadUi

gui, _ = loadUiType('gui.ui')


def info_btn_clicked():
    info_dialog = Info()
    info_dialog.exec_()


class Merger(QMainWindow, gui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actions_triggered()
        self.buttons_clicked()

    def buttons_clicked(self):
        self.addPDFButton.clicked.connect(self.getfile)

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)

    def getfile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "PDF files (*.pdf)")


class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()
        loadUi('info.ui', self)


def main():
    app = QApplication(sys.argv)
    window = Merger()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

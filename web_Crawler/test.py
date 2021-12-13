import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow

from crawler import *

ui = uic.loadUiType('app.ui')[0]
class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.crawler=GoogleWeather()
    
    def run(self):
        keyword = self.lineEdit.text()
        self.crawler.set_keyword(keyword+'날씨')
        self.crawler.run()
        res = self.crawler.get_result()
        print(res)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()

#출처 : https://jvvp.tistory.com/1063 (크롤러)
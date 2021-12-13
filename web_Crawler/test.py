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
        self.table_cols = ['지역','시간', '상태']
    
    def run(self):
        keyword = self.lineEdit.text()
        self.crawler.set_keyword(keyword+'날씨')
        self.crawler.run()
        res = self.crawler.get_result()
        self.set_table(res)
    
    def set_table(self, data):
        if data:
            row_idx = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_idx)

            col_idx = self.table_cols.index('지역')
            table_item = QtWidgets.QTableWidgetItem(data['loc'])
            self.tableWidget.setItem(row_idx,col_idx,table_item)

            col_idx = self.table_cols.index('시간')
            table_item = QtWidgets.QTableWidgetItem(data['time'])
            self.tableWidget.setItem(row_idx,col_idx,table_item)

            col_idx = self.table_cols.index('상태')
            table_item = QtWidgets.QTableWidgetItem(data['status'])
            self.tableWidget.setItem(row_idx,col_idx,table_item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()

# 필요한 모듈 pyqt5, pyqt5 pyqt5-tools
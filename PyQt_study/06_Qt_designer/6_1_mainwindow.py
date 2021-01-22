"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


form_class = uic.loadUiType('untitled.ui')[0]
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.click_event)

    def click_event(self):
        print('click')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLabel


def pixmap_event():
    global label

    pixmap = QPixmap('')
    label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    label = QLabel("Lable")
    button = QPushButton('Button')

    label.show()
    button.show()

    button.clicked.connect(pixmap_event)

    app.exec_()  # 이벤트 루프 실행
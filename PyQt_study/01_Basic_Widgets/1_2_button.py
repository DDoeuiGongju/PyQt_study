import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton


def button_event():
    print("button click")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    button = QPushButton("Button")
    button.show()

    button.clicked.connect(button_event)  # 버튼이 눌렸을때 문구가 뜨도록

    app.exec_()  # 이벤트 루프 실행
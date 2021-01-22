import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLabel


def label_event(text):
    global label
    label.setText(text + "!!!!")

def event():
    global label   # 전역변수를 한수 내에서 사용하기 위함

    str = label.text()   # 라벨의 글자를 가져옴
    str = str + '!!!'    # 버튼 클릭시 라벨의 글자에 !!!이 붙도록
    label.setText(str)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    label = QLabel("Text")
    label.show()

    # color: 글자의 색, background-color: 라벨의 배경색(16진수)
    label.setStyleSheet("color: white; background-color: #0000ff")

    button = QPushButton('Button')   # 버튼 추가
    button.show()

    button.clicked.connect(event)

    app.exec_()  # 이벤트 루프 실행
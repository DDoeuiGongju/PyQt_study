import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QCheckBox

def checkbox_event():
    global checkbox

    state = checkbox.isChecked()   # 체크 상태 받아오기
    text = checkbox.text()         # 체크 박스 글자 받아오기
    print(state, text)
    checkbox.setText(text + '!!!')

def event():
    global checkbox
    state = checkbox.isChecked()
    if state:
        print('눌림')
    else:
        print('안눌림')

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    checkbox = QCheckBox('Check Box')
    checkbox.show()
#    checkbox.clicked.connect(checkbox_event)

    # 버튼이 눌렸을 때 체크박스의 상태 받아오기
    button = QPushButton('Button')   # 버튼 추가
    button.show()
    button.clicked.connect(event)


    app.exec_()  # 이벤트 루프 실행
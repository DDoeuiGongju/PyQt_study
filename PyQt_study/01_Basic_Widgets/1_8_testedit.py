import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QTextEdit

def text_edit_event():
    global text_edit

    # 버튼 누르면 입력되었던 글자는 출력되고 지워짐
    print(text_edit.text())
    text_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    text_edit = QTextEdit()
    text_edit.show()

    button = QPushButton('Button')  # 버튼 추가
    button.show()
    button.clicked.connect(text_edit_event)

    app.exec_()  # 이벤트 루프 실행
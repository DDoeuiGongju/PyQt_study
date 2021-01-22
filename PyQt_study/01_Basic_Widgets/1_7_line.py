import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLineEdit

def line_edit_event():
    global line_edit

    # 버튼 누르면 입력되었던 글자는 출력되고 지워짐
    print(line_edit.text())
    line_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    line_edit = QLineEdit()
    line_edit.show()

    button = QPushButton('Button')  # 버튼 추가
    button.show()
    button.clicked.connect(line_edit_event)

    app.exec_()  # 이벤트 루프 실행
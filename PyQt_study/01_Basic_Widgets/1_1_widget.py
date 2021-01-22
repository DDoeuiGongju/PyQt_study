import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)   # QApplication생성

    widget = QWidget()        # 기본 위젯창 생성. 기능들을 상속받아 사용
    widget.show()

    widget.setWindowTitle("GUIprogram")   # 위젯창의 이름 설정

    # widget.move(200, 200)     # 위젯창의 위치 x, y
    # widget.resize(200, 200)   # 위젯의 크기 w, h

    widget.setGeometry(200, 200, 400, 400)   # x, y, w, h

    app.exec_()   # 이벤트 루프 실행


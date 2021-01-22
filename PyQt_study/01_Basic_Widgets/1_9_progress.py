import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QProgressBar

def progress_event():
    global progress

    val = progress.value()
    progress.setValue(val + 10)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    progress = QProgressBar()

    progress.setRange(1, 100)
    # progress.setRange(1, 100)   # 이렇게 하면 진행중임을 표시할 수 있다.
    progress.reset()

    progress.show()

    # 버튼이 눌렸을떄 프로그레스가 하나씩 진행되도록
    button = QPushButton('Button')  # 버튼 추가
    button.show()
    button.clicked.connect(progress_event)

    app.exec_()  # 이벤트 루프 실행
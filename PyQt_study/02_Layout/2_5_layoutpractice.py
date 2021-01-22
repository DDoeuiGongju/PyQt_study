"""
 * Requirements
pip install PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()   # Qwidget함수의 생성자함수(__init__) 실행
        main_layout = QVBoxLayout(self)
        layout = QHBoxLayout()

        label1 = QLabel("label1")
        label2 = QLabel("label2")
        label3 = QLabel("label3")

        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:orange")
        label3.setStyleSheet("background-color:yellow")

        main_layout.addWidget(label1)
        # 가로로 넣고싶은 레이아웃을 쌓고 상위 레이아웃에 넣는다
        layout.addWidget(label2)
        layout.addWidget(label3)
        main_layout.addLayout(layout)

# Layout 중첩, QWidget 상속
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = QWidget()
    # 상속시켜서 코드를 기능별로 분리해 메인함수 깔끔하게 만들귕
    window = MainWindow()
    window.show()

    app.exec_()

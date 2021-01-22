"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 임의의 빈 위젯
    window = QWidget()
    window.resize(500, 500)

    # 일일이 위치를 지정해주지 않아도 되도록
    # 위젯을 순차적으로 하나씩 쌓는다.
    layout = QHBoxLayout(window)
    window.setLayout(layout)

    label1 = QLabel("label1")
    label2 = QLabel("label2")
    label3 = QLabel("label3")
    # 색상 지정
    label1.setStyleSheet("background-color:red")
    label2.setStyleSheet("background-color:orange")
    label3.setStyleSheet("background-color:yellow")

    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)

    window.show()

    app.exec_()
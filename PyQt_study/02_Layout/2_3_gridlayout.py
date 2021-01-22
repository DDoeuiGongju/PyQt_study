"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(500, 500)

    # 리니어는 일렬로 나열하는 것이었는데 그리드는 바둑판모양으로 나열한다.
    layout = QGridLayout(window)
    window.setLayout(layout)

    label1 = QLabel("label1", window)
    label2 = QLabel("label2", window)
    label3 = QLabel("label3", window)

    label1.setStyleSheet("background-color:red")
    label2.setStyleSheet("background-color:orange")
    label3.setStyleSheet("background-color:yellow")

    # 행렬정보를 입력해야한다.
    layout.addWidget(label1, 0, 0)
    layout.addWidget(label2, 0, 1)
    # layout.addWidget(label3, 1, 0)
    layout.addWidget(label3, 1, 0, 1, 2)
    # 시작좌표, 행방향 몇칸 열방향 몇칸

    window.show()

    app.exec_()
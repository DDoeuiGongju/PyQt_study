"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 위젯을 상속해 버튼 위젯을 추가
    window = QWidget()
    window.resize(500, 500)

    button = QPushButton('Button', window)
    button.move(100, 100)

    window.show()
    app.exec_()
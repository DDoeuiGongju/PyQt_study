"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QPushButton
from PyQt5.QtWidgets import QVBoxLayout



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        # Actions
        # 아이콘 만들기: 아이콘 파일, 액션이 하는 기능 설명하는 글귀
        self.action_load = QAction(QIcon('../images/icons/save.png'), 'Load file', self)
        # 단축키
        self.action_load.setShortcut('Ctrl+L')
        # 액션이 하는 기능에 대한 함수
        self.action_load.triggered.connect(self.load_event)

        self.action_exit = QAction(QIcon('../images/icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('ESC')
        self.action_exit.triggered.connect(self.close)

        # Status bar
        # QMainWindow의 statusBar기능 사용
        self.status_bar = self.statusBar()

        # Menu bar
        # QMainWindow의 menuBar기능 사용
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('File')
        self.option_menu = self.menu_bar.addMenu('Options')
        self.help_menu = self.menu_bar.addMenu('Help')

        # file_menu에 액션 추가
        self.file_menu.addAction(self.action_load)
        self.file_menu.addAction(self.action_exit)

        # Tool bar
        # QMainWindow의 addToolBar기능 사용
        self.tool_bar = self.addToolBar("Toolbar")
        # 바로 액션 추가
        self.tool_bar.addAction(self.action_load)
        self.tool_bar.addAction(self.action_exit)

        # Central Widget
        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)
        window_layout.addWidget(QPushButton("Button"))
        # QMainWindow의 setCentralWidget기능 사용
        # 위젯 안에 위젯을 넣어줌
        self.setCentralWidget(window_widget)

    def load_event(self):
        # showMessage: 단순히 글귀 띄움
        # 파일 누르면 로드파일이라는 상태 글귀가 적힌다.
        self.status_bar.showMessage("Load file..")
        path = QFileDialog.getOpenFileName(self)
        print(path)
        # clearMessage: 글귀 지움
        self.status_bar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
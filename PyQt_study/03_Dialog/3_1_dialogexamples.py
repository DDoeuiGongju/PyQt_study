"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Message box
        self.button_message_box = QPushButton('Message box')
        self.layout.addWidget(self.button_message_box)
        self.button_message_box.clicked.connect(self.message_box_event)

        # Input dialog: 입력받깅~
        self.button_input_dialog = QPushButton('Input dialog')
        self.label_text = QLabel()
        self.layout.addWidget(self.button_input_dialog)
        self.layout.addWidget(self.label_text)
        self.button_input_dialog.clicked.connect(self.input_dialog_event)

        # File dialog
        self.button_file_dialog = QPushButton('File dialog')
        self.label_image = QLabel()
        self.pixmap = QPixmap()
        self.layout.addWidget(self.button_file_dialog)
        self.layout.addWidget(self.label_image)
        self.button_file_dialog.clicked.connect(self.file_dialog_event)

    def message_box_event(self):
        # 천번쨰 텍스트는 메세지창 제목, 두번째는 메세지 내용
        # .about: 단순한 정보전달
        QMessageBox.about(self, 'About box', 'Message')

        # | 표시로 속성에 따른 버튼 만들기, 기본 선택되어있을 버튼 지정
        # 한 단락에 각각의 메세지박스를 띄우는 방법이 들어가있다.
        # if문은  선택된 버튼에 따른 동작
        # .information: 파란 느낌표 정보 전달
        ret = QMessageBox.information(self, 'Information box', 'Message', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            print('Information box : ok')
        elif ret == QMessageBox.Cancel:
            print('Information box : cancel')

        # .warning: 노란 세모 느낌표로 경고 표시
        ret = QMessageBox.warning(self, 'Warning box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Discard)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel')

        # .question: 파란 물음표
        ret = QMessageBox.question(self, 'Question box', 'Message', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print('Question box : yes')
        elif ret == QMessageBox.No:
            print('Question box : no')

        # .critical: 빨간 엑스
        ret = QMessageBox.critical(self, 'Critical box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel')

    def input_dialog_event(self):
        text, ret = QInputDialog.getText(self, 'Input dialog', 'input : ')
        # 입력이 제대로 되어 ok를 누르면 true
        # 입력된 텍스트를 받아온다
        if ret:
            self.label_text.setText(text)

    def file_dialog_event(self):
        ret = QFileDialog.getOpenFileName(self, 'Select file')
        print(ret)

        path = ret[0]
        self.pixmap.load(path)
        self.label_image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
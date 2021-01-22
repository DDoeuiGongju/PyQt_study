"""
 * Requirements
pip install PyQt5
pip install opencv-python
"""

import sys
# 파이썬에서 제공하는 스레드 모듈
import threading

import cv2
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType('window.ui')[0]
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.capture = True
        self.thread = threading.Thread(target=self.video_capture_process)
        self.thread.start()

    def video_capture_process(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.capture:
            ret, frame = cap.read()
            self.set_image(frame)
        cap.release()

    def set_image(self, frame):
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(image)
        self.label_image.setPixmap(pixmap)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.capture = False
        # main이 끝나도 스레드가 끝날떄까지 기다린 후 join이후를 실행
        self.thread.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

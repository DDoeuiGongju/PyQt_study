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

form_class = uic.loadUiType('window.ui')[0]   # 미리 만들어놓은 ui파일
# ui파일을 상속받아서 사용
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 이 변수를 통해 프로그램이 끝나면 스레드도 끝나도록 해 줄 것이다.
        self.capture = True
        # 파이썬에서 제공하는 스레드 함수
        self.thread = threading.Thread(target=self.video_capture_process)
        # 스레드 실행(target함수 실행)
        self.thread.start()

    def video_capture_process(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.capture:
            ret, frame = cap.read()
            # 만든 gui에 이미지가 포함되도록 cv2.imshow 대신에 만든 함수
            self.set_image(frame)
        cap.release()

    def set_image(self, frame):
        # numpy array를 pyqt에서 지원하는 이미지 형태로 바꿔준다
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(image)
        self.label_image.setPixmap(pixmap)

    # QMainWindow가 기본적으로 가지고있는 함수로 창이 닫힌다는 이벤트가 발생했을때 실행
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # 스레드의 while문이 끝나게 한다.
        self.capture = False
        # 스레드가 끝날때까지 기다린 후 join 이후를 실행해 메인보다 늦게 끝나지 않도록 한다.
        self.thread.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

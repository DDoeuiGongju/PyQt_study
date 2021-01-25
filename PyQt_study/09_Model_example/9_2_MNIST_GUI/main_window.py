"""
 * Requirements

pip install PyQt5
pip install opencv-python

https://pytorch.org/

conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
or
conda install pytorch torchvision torchaudio cpuonly -c pytorch

"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from test_tab import TabTest
from train_tab import TabTrain

form_class = uic.loadUiType('ui/main_window.ui')[0]
class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 탭 추가(다른 파이썬파일에서 클래스 불러옴)
        # statusBar를 사용하기 위햇는 메인 윈도우의 statusBar를 받아가야 한다.
        self.tab_train = TabTrain(self.statusBar())
        self.tab_test = TabTest(self.statusBar())

        self.tab_widget.addTab(self.tab_train, "Train")
        self.tab_widget.addTab(self.tab_test, "Test")

        # 어느 탭이 선택된 상태로 뜨게 할 것인지
        self.tab_widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

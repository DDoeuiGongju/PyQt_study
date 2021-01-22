import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QSlider

def slider_horizon_event():
    global slider_horizon
    print(slider_horizon.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    # Qt.Horizontal: 가로 바 생성
    slider_horizon = QSlider(Qt.Horizontal)

    slider_horizon.setRange(0, 200)
    # 슬라이더의 값이 바뀌었을때 이벤트 발생
    slider_horizon.valueChanged.connect(slider_horizon_event)

    slider_horizon.show()

    app.exec_()  # 이벤트 루프 실행
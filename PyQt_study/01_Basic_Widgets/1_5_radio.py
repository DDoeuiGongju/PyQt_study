import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QRadioButton, QButtonGroup

def radio1_event():
    global group1
    # 체크한 버튼의 id, 체크한 버튼의 글자 가져오기
    print("버튼 ID:", group1.checkedId(), " 버튼 text:", group1.checkedButton().text())

def radio2_event():
    global group2
    print("버튼 ID:", group2.checkedId(), " 버튼 text:", group2.checkedButton().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    # QRadioButton: 일반적으로 여러 기능 중 한가지를 선택하는 경우 사용
    radio1_1 = QRadioButton('Radio 1_1')
    radio1_2 = QRadioButton('Radio 1_2')
    radio2_1 = QRadioButton('Radio 2_1')
    radio2_2 = QRadioButton('Radio 2_2')

    # 위젯 위치 및 크기 설정
    radio1_1.setGeometry(250, 100, 200, 50)
    radio1_2.setGeometry(500, 100, 200, 50)
    radio2_1.setGeometry(750, 100, 200, 50)
    radio2_2.setGeometry(1000, 100, 200, 50)

    # 버튼을 묶어줌(그룹 내 하나만 선택 가능)
    group1 = QButtonGroup()
    group1.addButton(radio1_1, 1)
    group1.addButton(radio1_2, 2)

    group2 = QButtonGroup()
    group2.addButton(radio2_1, 1)
    group2.addButton(radio2_2, 2)

    radio1_1.show()
    radio1_2.show()
    radio2_1.show()
    radio2_2.show()

    group1.buttonClicked.connect(radio1_event)
    group2.buttonClicked.connect(radio2_event)
    app.exec_()  # 이벤트 루프 실행
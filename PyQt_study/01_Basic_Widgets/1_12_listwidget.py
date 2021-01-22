import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget

def click_event():
    global list_widget
    # 아이템은 텍스트정보가 아닌 아이템의 객체정보다.
    print(list_widget.currentItem().text())
    print(list_widget.currentItem())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    list_widget = QListWidget()
    list_widget.doubleClicked.connect(click_event)
    items = ['1', '2', '3', '4']
    for item in items:
        list_widget.addItem(item)
    list_widget.show()

    app.exec_()  # 이벤트 루프 실행
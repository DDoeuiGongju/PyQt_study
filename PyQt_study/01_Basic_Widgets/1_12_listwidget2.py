import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    list_widget = QListWidget()

    for i in range(10):
        item = QListWidgetItem()
        button = QPushButton('Button'+str(i+1))
        # 일단 아이템을 넣어줌
        list_widget.addItem(item)
        # 아이템과 위젯 연결시켜줌
        list_widget.setItemWidget(item, button)
    list_widget.show()

    app.exec_()  # 이벤트 루프 실행
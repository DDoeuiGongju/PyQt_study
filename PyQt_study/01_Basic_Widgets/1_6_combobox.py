import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox

def combobox_event():
    global combobox

    index = combobox.currentIndex()
    text = combobox.currentText()
    print(index, ':', text)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication생성

    combobox = QComboBox()
    combobox_items = ['1', '2', '3', '4']
    for item in combobox_items:
        combobox.addItem(item)
    combobox.show()

    combobox.currentIndexChanged.connect(combobox_event)

    app.exec_()  # 이벤트 루프 실행
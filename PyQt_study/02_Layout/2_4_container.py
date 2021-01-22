"""
 * Requirements
pip install PyQt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QScrollArea, QWidget, \
    QHBoxLayout, QTabWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(400, 400)
    window.show()

    main_layout = QHBoxLayout()
    window.setLayout(main_layout)

    # Group box: 포함되는 위젯들의 역할을 명시줄 수 있는 디자인 요소
    group_box = QGroupBox('Group name')
    # 그룹박스에 포함시킬 레이아웃
    group_layout = QVBoxLayout(group_box)
    # group_layout = QHBoxLayout(group_box)   # 위젯 가로로 배치
    # 그룹박스에 포함
    group_layout.addWidget(QPushButton('Group box button'))
    main_layout.addWidget(group_box)

    # Scroll area: 스크롤 기능 넣어줌
    scroll_area = QScrollArea()
    label = QLabel("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz")
    scroll_area.setWidget(label)
    main_layout.addWidget(scroll_area)
    # main_layout.addWidget(label)

    # Tab
    tab_widget = QTabWidget()
    # 텝1에는 버튼 위젯만 추가
    tab1 = QPushButton('Tab1 button')
    tab_widget.addTab(tab1, 'Tab 1')

    # 텝2에는 레이블과 버튼 위젯 추가
    tab2 = QWidget()
    tab_layout = QVBoxLayout(tab2)
    tab_layout.addWidget(QLabel('Tab2 label'))
    tab_layout.addWidget(QPushButton('Tab2 button'))
    tab_widget.addTab(tab2, 'Tab 2')

    main_layout.addWidget(tab_widget)

    app.exec_()

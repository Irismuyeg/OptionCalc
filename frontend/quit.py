# -*-coding:utf-8-*-
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLabel


def quit(page):
    # title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" Exit")
    page.grid.addWidget(label_main, 0, 0)
    # text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      My work here is done!\n      Suppose yours is NOT.")
    page.grid.addWidget(label_content, 1, 0)
    # empty
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 2, 0, 2, 1)
    # title
    qbtn = QPushButton('BYEBYE!')
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.setStyleSheet('''
        QPushButton:hover{color:red}
        QPushButton{font-size:30px;
                    font-weight:200;
        }''')
    page.grid.addWidget(qbtn, 4, 0)

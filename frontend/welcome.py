# -*-coding:utf-8-*-
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QPropertyAnimation,QRect

def welcome(page):
    # title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" Ohhhh You are here again.")
    page.grid.addWidget(label_main, 0, 0)
    # text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("               I'm an option price calculator.")
    page.grid.addWidget(label_content, 1, 0)
    # # 开始探索图片
    # hint = QLabel()
    # directory = "img/hint.png"
    # pix = QPixmap()
    # pix.load(directory)
    # hint.setPixmap(pix)
    # page.grid.addWidget(hint, 2, 0, 1, 1)
    # Empty
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 4, 0)

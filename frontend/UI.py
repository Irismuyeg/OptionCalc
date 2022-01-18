# -*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QDesktopWidget,
                             QMessageBox, QMainWindow, QGridLayout, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
import page
import quit
import welcome
# import strat_input
import input
import backtest_result
import result
import qtawesome
# import pic_UI


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        self.widget = QWidget()
        self.widget.setObjectName("main")
        self.widget.setLayout(grid)
        self.setCentralWidget(self.widget)
        grid.setSpacing(20)

        # 这里是左侧的一堆功能键
        self.btn_welcome = QPushButton(qtawesome.icon('fa.sellsy'), 'Welcome', self)
        self.btn_welcome.clicked[bool].connect(self.button_clicked)
        self.btn_welcome.setObjectName("left")
        self.btn_input = QPushButton(qtawesome.icon('fa.music'), 'Option Parameters', self)
        self.btn_input.clicked[bool].connect(self.button_clicked)
        self.btn_input.setObjectName("left")
        self.btn_result = QPushButton(qtawesome.icon('fa.download'), 'Option Price', self)
        self.btn_result.clicked[bool].connect(self.button_clicked)
        self.btn_result.setObjectName("left")
        self.btn_result.setEnabled(False)
        self.btn_strat_input = QPushButton(qtawesome.icon('fa.film'), 'Back-test Parameters', self)
        self.btn_strat_input.clicked[bool].connect(self.button_clicked)
        self.btn_strat_input.setObjectName("left")
        self.btn_backtest = QPushButton(qtawesome.icon('fa.star'), 'Back-test Results', self)
        self.btn_backtest.clicked[bool].connect(self.button_clicked)
        self.btn_backtest.setObjectName("left")
        self.btn_backtest.setEnabled(False)
        self.btn_quit = QPushButton(qtawesome.icon('fa.question'), 'Exit', self)
        self.btn_quit.clicked[bool].connect(self.button_clicked)
        self.btn_quit.setObjectName("left")
        grid.addWidget(self.btn_welcome, 4, 0)
        grid.addWidget(self.btn_input, 5, 0)
        grid.addWidget(self.btn_result, 6, 0)
        grid.addWidget(self.btn_strat_input, 7, 0)
        grid.addWidget(self.btn_backtest, 8, 0)
        grid.addWidget(self.btn_quit, 9, 0)

        # every page of the buttons
        self.page_welcome = page.page(grid, self)
        welcome.welcome(self.page_welcome)
        self.page_result = page.page(grid, self)
        result.result(self.page_result)
        self.page_backtest = page.page(grid, self)
        backtest_result.result(self.page_backtest)
        self.page_quit = page.page(grid, self)
        quit.quit(self.page_quit)
        self.page_input = page.page(grid, self)
        input.input(self.page_input)
        self.page_strat_input = page.page(grid, self)
        input.strat_input(self.page_strat_input)
        self.page_welcome.show(self)

        # # 给布局添加上左侧功能键和LOGO
        # logo = QLabel(self)
        # directory = "img/logo2.png"
        # pix = QPixmap(directory)
        # logo.setPixmap(pix)
        # grid.addWidget(logo, 1, 0, 3, 1)

        # # 设置标题logo
        # self.setWindowIcon(QIcon(directory))
        # 居中并绘制
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('MiniCalculator')
        # # 导入qss样式
        # directory = "style.qss"
        # with open(directory, 'r') as f:
        #     qss_style = f.read()
        # self.setStyleSheet(qss_style)
        self.show()
        self.button_change(self.btn_welcome)

    def button_change(self, btn):
        self.btn_welcome.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_input.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_result.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_strat_input.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_backtest.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_quit.setStyleSheet('''QPushButton#left{background-color:}''')
        btn.setStyleSheet('''QPushButton#left{background-color:white;
                            border-color: red;
                            }''')

    # 按下左侧功能键的效果
    def button_clicked(self):
        sender = self.sender()
        if sender.text() == 'Welcome':
            self.page_welcome.show(self)
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            self.button_change(self.btn_welcome)
        if sender.text() == 'Option Parameters':
            self.page_input.show(self)
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_input)
        if sender.text() == 'Option Price':
            self.page_result.show(self)
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_result)
        if sender.text() == 'Back-test Parameters':
            self.page_strat_input.show(self)
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            # input.strat_input(self.page_strat_input)
            self.button_change(self.btn_strat_input)
        if sender.text() == 'Back-test Results':
            self.page_backtest.show(self)
            QApplication.processEvents()
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_backtest)
        if sender.text() == 'Exit':
            self.page_quit.show(self)
            # self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_quit)

    # 按退出键弹出确认窗口
    def close_event(self, event):

        reply = QMessageBox.question(self, 'Exit',
                                     "Are you sure to quit MiniSQL?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 启动时居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    QApplication.processEvents()
    app = QApplication(sys.argv)
    ex = MainWindow()
    # q = pic_UI.MainWindow()
    sys.exit(app.exec_())
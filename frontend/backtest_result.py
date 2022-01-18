# -*-coding:utf-8-*-
from PyQt5.QtWidgets import QLabel, QLineEdit, QApplication, QPushButton
from PyQt5.QtGui import *
# import os


# from PyQt5.QtCore import *



def result(page):
    # label_main = QLabel()
    # page.grid.addWidget(label_main, 0, 0, 1, 4)
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("Back-test Results")
    page.grid.addWidget(label_main, 0, 0, 1, 4)

    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("Annual-Portfolio Sharpe Ratio\n"
                          "(Final)")
    page.grid.addWidget(label_content, 1, 0)
    page.line_dr = QLineEdit(page.widget)
    page.line_dr.setEnabled(False)
    page.line_dr.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_dr, 1, 1)


    #SPY sr
    label_spy_sr = QLabel()
    label_spy_sr.setFont(page.font_content)
    label_spy_sr.setText('Annual-SPY Sharpe Ratio\n'
                         '(Final)')
    page.grid.addWidget(label_spy_sr, 1, 2)
    page.line_spy_sr = QLineEdit(page.widget)
    page.line_spy_sr.setEnabled(False)
    page.line_spy_sr.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_spy_sr, 1, 3)


    # Final PnL
    label_final_pnl = QLabel()
    label_final_pnl.setFont(page.font_content)
    label_final_pnl.setText("Portfolio PnL\n"
                            "(Final)")
    page.grid.addWidget(label_final_pnl, 2, 0)
    page.line_final_pnl = QLineEdit(page.widget)
    page.line_final_pnl.setEnabled(False)
    page.line_final_pnl.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_final_pnl, 2, 1)

    #SPY PnL
    label_spy_pnl = QLabel()
    label_spy_pnl.setFont(page.font_content)
    label_spy_pnl.setText("SPY PnL\n"
                          "(Final)")
    page.grid.addWidget(label_spy_pnl, 2, 2)
    page.line_spy_pnl = QLineEdit(page.widget)
    page.line_spy_pnl.setEnabled(False)
    page.line_spy_pnl.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_spy_pnl, 2, 3)

    #Put PnL
    label_put_pnl = QLabel()
    label_put_pnl.setFont(page.font_content)
    label_put_pnl.setText("Put PnL\n"
                          "(Final)")
    page.grid.addWidget(label_put_pnl, 2, 4)
    page.line_put_pnl = QLineEdit(page.widget)
    page.line_put_pnl.setEnabled(False)
    page.line_put_pnl.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_put_pnl, 2, 5)

    # mdd
    label_mdd = QLabel()
    label_mdd.setFont(page.font_content)
    label_mdd.setText("Portfolio Maximum Drawdown\n"
                      "(Monthly Returns)")
    page.grid.addWidget(label_mdd, 3, 0)
    page.line_mdd = QLineEdit(page.widget)
    page.line_mdd.setEnabled(False)
    page.line_mdd.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_mdd, 3, 1)

    #Spy mdd
    label_spy_mdd = QLabel()
    label_spy_mdd.setFont(page.font_content)
    label_spy_mdd.setText("SPY Maximum Drawdown\n"
                      "(Monthly Returns)")
    page.grid.addWidget(label_spy_mdd, 3, 2)
    page.line_spy_mdd = QLineEdit(page.widget)
    page.line_spy_mdd.setEnabled(False)
    page.line_spy_mdd.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_spy_mdd, 3, 3)

    #VaR1
    label_var1 = QLabel()
    label_var1.setFont(page.font_content)
    label_var1.setText("Portfolio VaR(1%)")
    page.grid.addWidget(label_var1, 4, 0)
    page.line_var1 = QLineEdit(page.widget)
    page.line_var1.setEnabled(False)
    page.line_var1.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_var1, 4, 1)

    #VaR2
    label_var2 = QLabel()
    label_var2.setFont(page.font_content)
    label_var2.setText("Portfolio VaR(5%)")
    page.grid.addWidget(label_var2, 4, 2)
    page.line_var2 = QLineEdit(page.widget)
    page.line_var2.setEnabled(False)
    page.line_var2.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_var2, 4, 3)

    label_spy_var1 = QLabel()
    label_spy_var1.setFont(page.font_content)
    label_spy_var1.setText("SPY VaR(1%)")
    page.grid.addWidget(label_spy_var1, 5, 0)
    page.line_spy_var1 = QLineEdit(page.widget)
    page.line_spy_var1.setEnabled(False)
    page.line_spy_var1.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_spy_var1, 5, 1)


    label_spy_var2 = QLabel()
    label_spy_var2.setFont(page.font_content)
    label_spy_var2.setText("SPY VaR(5%)")
    page.grid.addWidget(label_spy_var2, 5, 2)
    page.line_spy_var2 = QLineEdit(page.widget)
    page.line_spy_var2.setEnabled(False)
    page.line_spy_var2.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_spy_var2, 5, 3)


    # 占空位
    label_blank = QLabel()
    page.grid.addWidget(label_blank,6,0,1,2)

    # QApplication.processEvents()

    # btn_update = QPushButton('Update')
    # page.grid.addWidget(btn_update, 4, 0, 1, 4)
    # btn_update.setStyleSheet('''
    #         QPushButton:hover{color:red}
    #         QPushButton{font-size:18px;
    #                     font-weight:200;
    #         }''')
    # btn_update.clicked.connect(pic.show())

    # # 二叉树价格
    # label_bt = QLabel()
    # label_bt.setFont(page.font_content)
    # label_bt.setText("      Binary Tree Model Price")
    # page.grid.addWidget(label_bt, 4, 0)
    # page.line_bt = QLineEdit(page.widget)
    # page.line_bt.setEnabled(False)
    # page.line_bt.setStyleSheet("QLineEdit{background-color:white;color:black}")
    # page.grid.addWidget(page.line_bt, 4, 1)
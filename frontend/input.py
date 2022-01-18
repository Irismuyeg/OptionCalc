# -*-coding:utf-8-*-
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateTimeEdit, QApplication
from PyQt5.QtCore import QDate, QDateTime, QTime


def input(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("Option Parameters")
    page.grid.addWidget(label_main, 0, 0, 1, 4)

    # 选择当前时间
    label_t0 = QLabel()
    label_t0.setFont(page.font_content)
    label_t0.setText("Start Date")
    page.grid.addWidget(label_t0, 1, 0)
    page.date_edit_t0 = QDateTimeEdit(QDate.currentDate(), page.widget)
    page.date_edit_t0.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t0.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t0, 1, 1)

    # 选择到期时间
    label_t1 = QLabel()
    label_t1.setFont(page.font_content)
    label_t1.setText("Expiration Date")
    page.grid.addWidget(label_t1, 1, 2)
    page.date_edit_t1 = QDateTimeEdit(QDate.currentDate().addDays(10), page.widget)
    page.date_edit_t1.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t1.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t1, 1, 3)

    # 期权类型 美式欧式
    label_european = QLabel()
    label_european.setFont(page.font_content)
    label_european.setText("Option Type")
    page.combo_european = QComboBox(page.widget)
    page.combo_european.addItem("European")
    page.combo_european.addItem("American")
    page.grid.addWidget(label_european, 2, 0)
    page.grid.addWidget(page.combo_european, 2, 1)

    # 期权类型 看涨看跌
    label_kind = QLabel()
    label_kind.setFont(page.font_content)
    label_kind.setText("Call or Put")
    page.combo_kind = QComboBox(page.widget)
    page.combo_kind.addItem("Call")
    page.combo_kind.addItem("Put")
    page.grid.addWidget(label_kind, 2, 2)
    page.grid.addWidget(page.combo_kind, 2, 3)

    # 标的资产现价
    label_s0 = QLabel()
    label_s0.setFont(page.font_content)
    label_s0.setText("Current Price of Underlying Asset")
    page.s0 = QLineEdit(page.widget)
    page.s0.setText('100')
    page.grid.addWidget(label_s0, 3, 0)
    page.grid.addWidget(page.s0, 3, 1)

    # 适用的波动率
    label_sigma = QLabel()
    label_sigma.setFont(page.font_content)
    label_sigma.setText("Annualized Volatility(%)")
    page.sigma = QLineEdit(page.widget)
    page.sigma.setText('1')
    page.grid.addWidget(label_sigma, 3, 2 )
    page.grid.addWidget(page.sigma, 3, 3)

    # 期权执行价
    label_k = QLabel()
    label_k.setFont(page.font_content)
    label_k.setText("Strike Price")
    page.k = QLineEdit(page.widget)
    page.k.setText('100')
    page.grid.addWidget(label_k, 4, 0)
    page.grid.addWidget(page.k, 4, 1)

    # 适用的无风险利率
    label_r = QLabel()
    label_r.setFont(page.font_content)
    label_r.setText("Annualized risk-free rate(%)")
    page.r = QLineEdit(page.widget)
    page.r.setText('1')
    page.grid.addWidget(label_r, 4, 2)
    page.grid.addWidget(page.r, 4, 3)

    # 股利
    label_dv = QLabel()
    label_dv.setFont(page.font_content)
    label_dv.setText("Annualized Dividend Rate(%)")
    page.dv = QLineEdit(page.widget)
    page.dv.setText('0')
    page.grid.addWidget(label_dv, 5, 0)
    page.grid.addWidget(page.dv, 5, 1)

    # 占空位
    label_blank = QLabel()
    page.grid.addWidget(label_blank,6,0,1,4)

    # 蒙特卡罗迭代次数
    label_mc = QLabel()
    label_mc.setFont(page.font_content)
    label_mc.setText("Monte Carlo Iteration")
    page.mc = QLineEdit(page.widget)
    page.mc.setText('100000')
    page.grid.addWidget(label_mc, 7, 0)
    page.grid.addWidget(page.mc, 7, 1)

    # 二叉树迭代次数
    label_bt = QLabel()
    label_bt.setFont(page.font_content)
    label_bt.setText("Binary Tree Iteration")
    page.bt = QLineEdit(page.widget)
    page.bt.setText('500')
    page.grid.addWidget(label_bt, 7, 2)
    page.grid.addWidget(page.bt, 7, 3)

    # 确定输入按键
    btn_confirm = QPushButton('Calculate')
    page.grid.addWidget(btn_confirm, 8, 0, 1, 4)
    btn_confirm.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    btn_confirm.clicked.connect(page.confirm)



def strat_input(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("Back-test Parameters")
    page.grid.addWidget(label_main, 0, 0, 1, 4)

    # 选择当前时间
    label_t0 = QLabel()
    label_t0.setFont(page.font_content)
    label_t0.setText("Start Date")
    page.grid.addWidget(label_t0, 1, 0)
    page.start_date = QDateTimeEdit(QDate.currentDate(), page.widget)
    page.start_date.setDisplayFormat('yyyy-MM-dd')
    page.start_date.setCalendarPopup(True)
    page.grid.addWidget(page.start_date, 1, 1)

    # 选择到期时间
    label_win = QLabel()
    label_win.setFont(page.font_content)
    label_win.setText("Back-test Window(Months)")
    page.grid.addWidget(label_win, 1, 2)
    # page.date_edit_t1 = QDateTimeEdit(QDate.currentDate().addDays(30), page.widget)
    # page.date_edit_t1.setDisplayFormat('yyyy-MM-dd')
    # page.date_edit_t1.setCalendarPopup(True)
    # page.grid.addWidget(page.date_edit_t1, 1, 3)
    page.period = QLineEdit(page.widget)
    page.period.setText('30')
    page.grid.addWidget(page.period, 1, 3)

    # strategy
    label_flag = QLabel()
    label_flag.setFont(page.font_content)
    label_flag.setText("Strategy")
    page.combo_flag = QComboBox(page.widget)
    page.combo_flag.addItem("OTM strategy")
    page.combo_flag.addItem("Delta Based Strategy")
    page.grid.addWidget(label_flag, 2, 0)
    page.grid.addWidget(page.combo_flag, 2, 1)

    # maturity
    label_maturity = QLabel()
    label_maturity.setFont(page.font_content)
    label_maturity.setText("Maturity(Months)")
    page.combo_maturity = QComboBox(page.widget)
    page.combo_maturity.addItem("1")
    page.combo_maturity.addItem("3")
    page.grid.addWidget(label_maturity, 2, 2)
    page.grid.addWidget(page.combo_maturity, 2, 3)

    # otm percentage
    label_otm_pct = QLabel()
    label_otm_pct.setFont(page.font_content)
    label_otm_pct.setText("Out-of-money Percentage(%)")
    page.otm_pct = QLineEdit(page.widget)
    page.otm_pct.setText('20')
    page.grid.addWidget(label_otm_pct, 3, 0)
    page.grid.addWidget(page.otm_pct, 3, 1)

    # delta
    label_delta = QLabel()
    label_delta.setFont(page.font_content)
    label_delta.setText("Delta Percentage(%)")
    page.delta = QLineEdit(page.widget)
    page.delta.setText('10')
    page.grid.addWidget(label_delta, 3, 2)
    page.grid.addWidget(page.delta, 3, 3)

    # 文字
    label_hint = QLabel()
    label_hint.setFont(page.font_content)
    label_hint.setText("  Assumptions: \n"
                       "\ta. \bBacktester period：2002-2021\n"
                       "\tb. \bNo trading cost\n"
                       "\tc. \bNo dividend rate\n"
                       "\td. \b1-month contract use 1-month swap rate as interest rate, \n"
                       "\t \b\b>1-month contract use 3 month swap rate as interest rate\n"
                       "\te. \bperiod greater than 12 months")
    page.grid.addWidget(label_hint, 4, 0, 1, 2)

    # 占空位
    label_blank = QLabel()
    page.grid.addWidget(label_blank,6,0,1,4)

    # 确定输入按键
    btn_confirm = QPushButton('Backtest')
    page.grid.addWidget(btn_confirm, 7, 0, 1, 4)
    btn_confirm.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    btn_confirm.clicked.connect(page.run)
    QApplication.processEvents()

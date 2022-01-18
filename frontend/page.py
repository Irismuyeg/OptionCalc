# -*-coding:utf-8-*-
import sys
from threading import Thread

sys.path.append("..")
from PyQt5.QtWidgets import (QWidget, QMessageBox, QGridLayout, QApplication)
from PyQt5.QtGui import QFont
from backend.Option import Option
import numpy as np
from backend.Backtest import Backtest
import datetime
# import pic_UI



class Calculatebt(Thread):

    def __init__(self, option, btstep):
        super().__init__()
        self.option = option
        self.btstep = btstep

    def run(self):
        self.option.bt_model(self.btstep)

class Calculatemc(Thread):

    def __init__(self, option, mcstep):
        super().__init__()
        self.option = option
        self.mcstep = mcstep

    def run(self):
        self.option.mc_model(self.mcstep)

class Calculatebs(Thread):

    def __init__(self, option):
        super().__init__()
        self.option = option

    def run(self):
        self.option.bs_model()

class Calculatebacktest(Thread):

    def __init__(self, backtest):
        super().__init__()
        self.backtest = backtest

    def run(self):
        self.backtest.run()

class page:
    def __init__(self, grid, mw):
        self.mw = mw
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setSpacing(25)
        self.widget.setLayout(self.grid)
        grid.addWidget(self.widget, 1, 1, 13, 4)
        # fonts
        self.font_main = QFont()
        # self.font_main.setFamily('微软雅黑')
        self.font_main.setPointSize(60)
        self.font_main.setWeight(40)

        self.font_content = QFont()
        # self.font_content.setFamily('微软雅黑')
        self.font_content.setPointSize(15)
        self.font_content.setWeight(40)
        # properties of parameters
        self.combo_kind = None
        self.combo_european = None
        self.s0 = None
        self.date_edit_t1 = None
        self.sigma = None
        self.date_edit_t0 = None
        self.r = None
        self.k = None
        self.dv = None
        self.bsprice = None
        self.mcprice = None
        self.btprice = None
        self.mc = None
        self.bt = None
        self.delta = None

        self.combo_maturity = None
        self.start_date = None
        self.period = None
        # self.end_date = None
        self.otm_pct = None
        self.daily_returns = None
        self.op_pos = None
        self.combo_flag = None
        self.delta = None
        # self.F = None


    def show(self, mw):
        mw.page_quit.widget.hide()
        mw.page_welcome.widget.hide()
        mw.page_input.widget.hide()
        mw.page_result.widget.hide()
        mw.page_strat_input.widget.hide()
        mw.page_backtest.widget.hide()
        self.widget.show()

    #  确认输入
    def confirm(self):
        try:
            if self.combo_kind.currentText() == "Call":
                kind = 1
            else:
                kind = -1
            if self.combo_european.currentText() == "American":
                european = False
            else:
                european = True
            s0 = float(self.s0.text())
            k = float(self.k.text())
            sigma = float(self.sigma.text()) / 100
            r = float(self.r.text()) / 100
            r = np.log(1 + r)
            t1 = self.date_edit_t1.date()
            t0 = self.date_edit_t0.date()
            t = t0.daysTo(t1)
            dv = float(self.dv.text()) / 100
            dv = np.log(1 + dv)
            mcstep = int(self.mc.text())
            btstep = int(self.bt.text())
            option = Option(european, kind, s0, k, t, r, sigma, dv)
            t1 = Calculatebs(option)
            t2 = Calculatebt(option,btstep)
            t3 = Calculatemc(option,mcstep)
            t1.start()
            t2.start()
            t3.start()
            QMessageBox.about(self.widget,
                              "Reminder",
                              "Calculating...\nPlease Don't Rush me！")

            t1.join()
            t2.join()
            t3.join()
            QMessageBox.about(self.widget,
                              "Reminder",
                              "Done!\nLet's check the price！")
            print(type(option.bsprice))
            self.mw.page_result.line_bs.setText(str(option.bsprice))
            self.mw.page_result.line_mc.setText(str(option.mcprice, ))
            self.mw.page_result.line_bt.setText(str(round(option.btprice, 2)))
            self.mw.page_result.show(self.mw)
            # self.mw.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.mw.button_change(self.mw.btn_result)
            self.mw.btn_result.setEnabled(True)
        except ValueError:
            QMessageBox.about(self.widget,
                              "Reminder",
                              "You input the wrong numbers...\nPlease check！")
        except ZeroDivisionError:
            QMessageBox.about(self.widget,
                              "Reminder",
                              "We need two different dates!\nVolatility can't be zero!\nStrike can't be zero!")

    def run(self):
        try:
            if self.combo_maturity.currentText() == "1":
                maturity = 1
            else:
                maturity = 3
            start_date = str(self.start_date.date().toPyDate())
            start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d')
            # start_date = datetime.datetime(start_date,'%m/%d/%Y')
            # print(start_date)
            period = int(self.period.text())

            # maturity = float(self.combo_maturity.text())

            otm_pct = float(self.otm_pct.text())
            delta = float(self.delta.text())

            if self.combo_flag.currentText() == "OTM strategy":
                flag = 0
            else:
                flag = 1

            # self.F = MyFigure(width=3, height=2, dpi=100)
            result = Backtest(start_date, period, otm_pct, maturity, flag, delta)
            result.run()


            QMessageBox.about(self.widget,
                              "Reminder",
                              "Calculating...\nPlease Don't Rush me！")

            QMessageBox.about(self.widget,
                              "Reminder",
                              "Done!\nLet's check the result！")


            self.mw.page_backtest.line_dr.setText(str(round(result.monthly_returns['sharpe ratio'].iloc[-1], 3)))
            self.mw.page_backtest.line_spy_sr.setText(str(round(result.monthly_returns['SPY sharpe ratio'].iloc[-1], 2)))
            # self.mw.page_backtest.line_sr.setText(str(round(result.monthly_returns['put sharpe ratio'].iloc[-1], 2)))
            self.mw.page_backtest.line_final_pnl.setText(str(round(result.pnl, 2))+'%')
            self.mw.page_backtest.line_spy_pnl.setText(str(round(result.spypnl, 2))+'%')
            self.mw.page_backtest.line_put_pnl.setText(str(round(result.putpnl, 2))+'%')
            self.mw.page_backtest.line_mdd.setText(str(round(result.max_drawdown['monthly returns']*100, 2)) + '%')
            self.mw.page_backtest.line_spy_mdd.setText(str(round(result.max_drawdown['monthly SPY returns']*100, 2)) + '%')
            self.mw.page_backtest.line_var1.setText(str(result.VaR_1)+'%')
            self.mw.page_backtest.line_var2.setText(str(result.VaR_2)+'%')
            self.mw.page_backtest.line_spy_var1.setText(str(result.VaR_SPY_1)+'%')
            self.mw.page_backtest.line_spy_var2.setText(str(result.VaR_SPY_2)+'%')

            self.mw.page_backtest.show(self.mw)
            # self.mw.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.mw.button_change(self.mw.btn_backtest)
            self.mw.btn_backtest.setEnabled(True)
        except ValueError:
            QMessageBox.about(self.widget,
                              "Reminder",
                              "You input the wrong numbers...\nPlease check！")
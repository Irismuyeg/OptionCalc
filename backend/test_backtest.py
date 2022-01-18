# -*-coding:utf-8-*-
import math
from scipy.stats import norm
import numpy as np
import pandas as pd
import Option
from dateutil.relativedelta import relativedelta
import datetime
import matplotlib.pyplot as plt
import Backtest

def test(start_date, period, otm_pct, maturity, flag, delta):
    result = Backtest.Backtest(start_date, period, otm_pct, maturity, flag, delta)
    result.run()
    print('daily_returns:\n', result.daily_returns[['daily PnL', 'daily SPY PnL', 'daily Put PnL']])
    print('monthly_returns:\n', result.monthly_returns)
    print('mdd:\n', result.max_drawdown)
    print('annual returns:\n', result.annual_return)
    print('annual SPY returns\n', result.annual_SPY_return)
    print('VaR(1) with Strategy: %.4f'% result.VaR_1)
    print('VaR(5) with Strategy: %.4f'% result.VaR_2)
    print('VaR(1) with SPY: %.4f'% result.VaR_SPY_1)
    print('VaR(5) with SPY: %.4f'% result.VaR_SPY_2)

start_date = datetime.datetime.strptime('01/01/2015','%m/%d/%Y')
test(start_date, 78, 20, 3, 1, 10)


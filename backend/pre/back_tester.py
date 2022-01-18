import math
from scipy.stats import norm
import numpy as np
import pandas as pd
# import option_Pricer
from dateutil.relativedelta import relativedelta
import datetime
import matplotlib.pyplot as plt
import option_pricer

def plot_returns(df, figure, maturity, OTM_pctg, flag, delta, df_SPY=None):
    df.index = df.index.strftime('%y-%m-%d')
    time = df.index.values
    t = range(0, len(time))
    plt.plot(t, df)
    if df_SPY is not None:
        plt.plot(t, df_SPY)
    timetic = list(range(0, len(time), len(time)//20))
    plt.xticks(timetic, labels=time[timetic], rotation=90, fontsize=7)
    plt.xlim(0, len(time))
    plt.grid(ls='-.')
    if df_SPY is not None:
        plt.legend(['Strategy PnL', 'SPY PnL'],loc='upper left',fontsize =10)
    else:
        plt.legend(df.columns,loc='upper left', fontsize =10)
    plt.xlabel('Date')
    if flag == 0:
        plt.title('Strategy: buy %d month put contract, using %d percentage OTM' % (maturity, OTM_pctg))
    if flag == 1:
        plt.title('Strategy: buy %d month put contract, using %d delta' % (maturity, delta))
    plt.savefig(figure+'.png')
    plt.show()

tmp_PnL = 0
tmp_Spy_PnL = 0
'''
Assumption
do not execute the option when it expires
so the portfolio value at the maturity day is SPY value
'''
def back_tester(start_time,end_time,SPY,SPY_position,Vol,r_f, OTM_pctg, flag, delta):
    global tmp_PnL,tmp_Spy_PnL,option_position
    option_price = []
    SPY = SPY.loc[start_time:end_time] # SPY price
    portfolio_value = np.multiply(SPY,SPY_position)

    # Calculate option price
    count = 0
    for date in SPY.index:
        S = SPY.loc[date].values[0]
        v = Vol.loc[date].values[0]
        r = r_f.loc[date].values[0]
        T = (end_time - date)/np.timedelta64(365, 'D')
        if count == 0:
            S_first = S
            v_first = v
            r_first = r
            T_first = T
        count += 1
        if flag == 0: # Using OTM strategy
            K = SPY.iloc[0].values[0]*((100-OTM_pctg)/100)
            put_price = option_pricer.put_price(S,K,v,r,T)
        elif flag == 1: # Using delta based strategy
            d1= option_pricer.delta_to_d1(delta)
            K = option_pricer.d1_to_k(d1, S_first, v_first, r_first, T_first) # K is constant
            put_price = option_pricer.put_price(S,K,v,r,T)
        option_price.append(put_price)

    # Calculate option position
    #SPY_position = 10**6/SPY.loc[start_time].values[0]
    print(option_price)
    Option_position = SPY_position/100
    daily_returns = pd.DataFrame(index=SPY.index)
    option_value_df = pd.DataFrame(100*np.multiply(option_price,Option_position),index= SPY.index,columns = ['Option Price'])
    Spy_PnL = tmp_Spy_PnL+portfolio_value - SPY_position*SPY.iloc[0].values[0]
    daily_returns['daily SPY returns'] = portfolio_value['Last Price'].pct_change().values

    portfolio_value = np.add(option_value_df, portfolio_value)
    PnL = tmp_PnL+portfolio_value-SPY_position*SPY.iloc[0].values[0]-100*option_price[0]*Option_position

    daily_returns['daily returns'] = portfolio_value['Option Price'].pct_change().values
    daily_returns['daily PnL'] = PnL
    daily_returns['daily SPY PnL'] = Spy_PnL
    tmp_Spy_PnL = daily_returns['daily SPY PnL'][-1]
    tmp_PnL = daily_returns['daily PnL'][-1]
    return daily_returns,Option_position

if __name__ == '__main__':
    # choose type of put option
    start_time = input('Start Date (mm/dd/yyyy):')
    start_time = datetime.datetime.strptime(start_time,'%m/%d/%Y')
    maturity = input('Contract time maturity (Month 1/3): ')
    maturity = eval(maturity)
    period = input('Back test period (Month):') #assume it is an integral multiple of Maturity
    period = eval(period)
    end_time = start_time+relativedelta(months = period)
    flag = input('Choose which strategy (0 for OTM, 1 for delta based): ' )
    flag = eval(flag)
    if flag == 0:
        OTM_pctg = input('OTM percentage (%):')
        OTM_pctg = eval(OTM_pctg)
        delta = 0
    elif flag == 1:
        OTM_pctg = 0
        delta = input('Delta: ')
        delta = eval(delta)

    # extract data
    SPY = pd.read_excel('data.xlsx',sheet_name='SPY',engine='openpyxl')
    SPY.set_index('Date',inplace = True)
    SPY = SPY.loc[start_time:end_time]
    SPY = SPY['Last Price'].to_frame()
    if maturity == 1:
        #for 1M maturity, we use VIX
        Vol = pd.read_excel('data.xlsx',sheet_name='VIX',engine='openpyxl')
    else:
        #for other maturities, we use VIX3 as vol
        Vol = pd.read_excel('data.xlsx', sheet_name='VIX3',engine='openpyxl')
    Vol.set_index('Date',inplace = True)
    Vol = Vol.loc[start_time:end_time]
    Vol = Vol*0.01
    r_f = pd.read_excel('data.xlsx', sheet_name='USSOC BGN Curncy(3M)',engine='openpyxl')
    r_f.set_index('Date',inplace = True)
    r_f = r_f*0.01*12
    r_f = r_f.loc[start_time:end_time]

    daily_returns = pd.DataFrame()
    pos_list = []
    SPY_position = 10**6/SPY.iloc[0].values[0]
    multiple = math.ceil(period/maturity)
    for i in range(multiple):
        tmp_time = start_time+relativedelta(months = maturity)
        if tmp_time > end_time:
            tmp_time = end_time
        tmp_daily_returns,op_pos = back_tester(start_time, tmp_time, SPY, SPY_position,Vol, r_f, OTM_pctg, flag, delta)
        daily_returns = pd.concat([daily_returns,tmp_daily_returns])
        start_time = tmp_time
        pos_list.append(op_pos)

    # annualized result
    daily_returns['mean'] = daily_returns['daily returns'].expanding().mean() *252
    daily_returns['volatility'] = daily_returns['daily returns'].expanding().std() * np.sqrt(252)
    daily_returns['sharpe ratio'] = daily_returns['mean'] / daily_returns['volatility']
    monthly_returns = pd.DataFrame()
    monthly_returns['monthly returns'] = (daily_returns['daily returns'] +1).resample('M').prod()
    monthly_returns['monthly returns'] = monthly_returns['monthly returns'] -1
    monthly_returns['monthly SPY returns'] = (daily_returns['daily SPY returns'] +1).resample('M').prod()
    monthly_returns['monthly SPY returns'] = monthly_returns['monthly SPY returns'] -1
    monthly_returns['mean'] = monthly_returns['monthly returns'].expanding().mean() *12
    monthly_returns['volatility'] = monthly_returns['monthly returns'].expanding().std() * np.sqrt(12)
    monthly_returns['sharpe ratio'] = monthly_returns['mean'] / monthly_returns['volatility']
    #monthly_returns['mean(SPY)'] = monthly_returns['monthly SPY returns'].expanding().mean() *12
    #monthly_returns['volatility(SPY)'] = monthly_returns['monthly SPY returns'].expanding().std() * np.sqrt(12)
    #monthly_returns['sharpe ratio(SPY)'] = monthly_returns['mean(SPY)'] / monthly_returns['volatility(SPY)']
    print(daily_returns)
    print(monthly_returns)
    cum_ret = (1 + monthly_returns[['monthly returns','monthly SPY returns']]).cumprod()
    rolling_max = cum_ret.cummax()
    drawdown = (cum_ret - rolling_max) / rolling_max
    max_drawdown = drawdown.min()
    print('Max Drawdown: ')
    print(max_drawdown)

    plot_returns(pd.DataFrame(monthly_returns['monthly returns']),'monthly_returns', maturity, OTM_pctg, flag, delta)
    plot_returns(pd.DataFrame(daily_returns['daily PnL']),'daily_PnL', maturity, OTM_pctg, flag, delta,
                 pd.DataFrame(daily_returns['daily SPY PnL']))
    plot_returns(pd.DataFrame(daily_returns['sharpe ratio']),'daily_SR', maturity, OTM_pctg, flag, delta)
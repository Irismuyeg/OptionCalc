# -*-coding:utf-8-*-
import numpy as np
from scipy.stats import norm
import math

# SPX: S&P 500 index
# strike: strike price of put option
# r_f: interest rate (1 month/3 month treasury rate)
# T: time to maturity
# vol: VIX/VIX3


def option_pricer(SPX, strike, r_f, T, vol):
    d1 = (np.log(SPX / strike) + (r_f + vol ** 2 / 2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    price = strike * np.exp(-r_f * T) * norm.cdf(-d2) - SPX * norm.cdf(-d1)
    return price


# 3. You won't need to implement the normal cumulative distribution function. It has been done for you, below.
# However if you are curious to look under the hood to understand the details, please visit:
# https://malishoaib.wordpress.com/2014/04/02/python-code-and-normal-distribution-writing-cdf-from-scratch/

def norm_cdf(x):
    return norm.cdf(x)


# 4. Create a function, d_i, that calculates d1 and d2 of the black-scholes option pricing formula. This function
# should be called in the following way.
# d1 = d_i(i, S, K, v, r, T); where the first argument specifies if you want to calculate d1 or d2. i.e. i = 1 or 2
# Also, see if you can implement this function in just one line of code.

# write function here
def d_i(i, S, K, v, r, T):
    d1 = (np.log(S / K) + (r + (v ** 2) / 2) * T) / (v * np.sqrt(T))
    tmp = v * np.sqrt(T)
    return d1 if i == 1 else d1 - tmp


# 5. Create a function that calculates a European call price.
# write function here
def call_price(S, K, v, r, T):
    d1 = d_i(1, S, K, v, r, T)
    d2 = d_i(2, S, K, v, r, T)
    price = norm_cdf(d1) * S - norm_cdf(d2) * K * np.exp(-r * T)
    return price

'''
S: stock price
K: strike price
v: volatility (% p.a.)
r = continuously compounded risk-free interest rate (% p.a.)
q = continuously compounded dividend yield (% p.a.) = 0
T = time to expiration (% of year)
'''

def put_price(S, K, v, r, T):
    d1 = d_i(1, S, K, v, r, T)
    d2 = d_i(2, S, K, v, r, T)
    price = norm_cdf(-d2) * K * np.exp(-r * T) - norm_cdf(-d1) * S
    return price

def delta_to_d1(delta):
    return -norm.ppf(delta/100)


def d1_to_k(d1,S,v,r,T):
    K = S / (np.exp(d1 * v * np.sqrt(T) - T * (r + (v**2) / 2)))
    return K
# -*-coding:utf-8-*-
import scipy.stats as st
import numpy as np

class Option:
    # European Options
    def __init__(self, euro, kind, S0, K, T, r, sigma, dv):
        self.euro = euro
        self.kind = kind
        self.S0 = S0
        self.K = K
        self.T = T/365
        self.r = r
        self.sigma = sigma
        self.dv = dv
        self.bsprice = None
        self.mtprice = None
        self.btprice = None
        self.nnprice = None
        self.delta = None


    def bs_model(self):
        if self.euro or self.kind == 1:
            d1 = (np.log(self.S0 / self.K) + (self.r - self.dv + .5 * (self.sigma ** 2)) * self.T) / (self.sigma * np.sqrt(self.T))
            d2 = d1 - self.sigma * np.sqrt(self.T)
            self.bsprice = round(self.kind * self.S0 * np.exp(-self.dv * self.T) * \
                           st.norm.cdf(self.kind * d1) - self.kind * self.K * np.exp(-self.r * self.T) * st.norm.cdf(self.kind * d2), 2)
            self.delta = self.kind * st.norm.cdf(self.kind * d1)
        else:
            self.bsprice = 'This is an American Option. Not suitable for BS model.'

    def mc_model(self, simulation):
        if self.euro or self.kind == 1:
            l = np.random.normal(0.0, 1.0, simulation)
            St = self.S0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.T + self.sigma * self.T ** .5 * l)
            St = np.maximum(self.kind * (St - self.K), 0)
            self.mcprice = round(np.average(St) * np.exp(-self.r * self.T), 2)
        else:
            self.mcprice = 'This is an American Option. Not suitable for MonteCarlo.'

    def bt_model(self, iteration):
        n = iteration
        delta = self.T/n
        u = np.exp(self.sigma * np.sqrt(delta))
        d = 1/u
        p = (np.exp((self.r - self.dv) * delta) - d)/(u-d)

        #stock price tree
        stock = np.zeros([n+1, n+1])
        for layer in range(n+1):
            for up in range(layer+1):
                stock[up, layer] = self.S0 * (u**up) * (d**(layer-up))

        #option price tree
        option = np.zeros([n+1, n+1])
        option[:, n] = np.maximum(np.zeros(n+1), (stock[:, n] - self.K)*self.kind)
        for layer in range(n-1, -1, -1):
            for up in range(layer+1):
                option[up, layer] = (p*option[up+1, layer+1] +
                                     (1-p)*option[up, layer+1])/(np.exp((self.r - self.dv) * delta))

        self.btprice = option[0, 0]

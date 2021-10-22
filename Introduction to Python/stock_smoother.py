#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import statsmodels.api as sm
import pandas as pd
import numpy as np
import statsmodels.api as sm   
import datetime as dt

import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
import seaborn as sns

from pandas_datareader import data

def smooth_lowess(y_series, lowess_window_length = 100, smoothing_iterations = 2):
    
    """
    This is a customized LOWESS (locally weighted scatterplot smoothing) implementation that "smooths" a discrete data set.  
    In the LOWESS, each smoothed value is given by a weighted linear least squares regression over the span.  
    
    This implementation uses an upstream process to account for missing and zero values and data series that can't have negative values.  
    It also allows for a finite window length above 3, rather than a percentage of the total dataset.   
    
    It uses the statstmodels implementation:
    statsmodels.nonparametric.smoothers_lowess.lowess
    source: https://www.statsmodels.org/stable/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html
    
    Params:
    
    y_series:  Pandas series of discrete points as the inputs variable y
    lowess_window_length:  This is the window length passed smoothed through the data set. It cannot be less than 3. 
    smoothing_iterations: number of times to iterate the smoother
    
    Returns:
    yhat: a Pandas series of the smoothed values.
    """
    
    y_series = y_series.fillna(0) # replace all NaN values with 0
    x_series = list(np.arange(0,len(y_series),1))
    
    window = lowess_window_length/len(x_series)
    
    
    lowess = sm.nonparametric.lowess
    smooth = lowess(y_series, x_series, frac = window, it = smoothing_iterations)
    index, yhat = np.transpose(smooth)
    
    return yhat

def plot_stock_trend(company, days_ago = 180, source = 'yahoo'):
    
    
    """
    Displays closing price trend of a given stock using a LOWESS smoother. 
    
    Params:
    
    company: (string) ticker symbol 
    days_ago: (integer) the number of days to look back
    source: (string) source of the financial data. 

    """
    
    #imports()
    end= pd.to_datetime("now")
    start= end - dt.timedelta(days= days_ago) 

    closing_prices = data.DataReader(company, source, start, end)['Close']
    smoothed_prices = smooth_lowess(closing_prices, lowess_window_length = 21)
    dates = closing_prices.index

    plt.style.context('ggplot')
    fig, ax = plt.subplots(figsize = (18,7), dpi = 200)

    fmt = '${x:,.0f}'
    tick = ticker.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick) 
    ax.tick_params(axis='y', labelsize = 14)
    ax.tick_params(axis='x', labelsize = 14)

    ax.set_title('\nLOWESS Smoothed Closing Prices for {}\n'.format(company), fontsize = 25)
    ax.set_xlabel('\nDate\n', fontsize = 20)
    ax.set_ylabel('\nPrice\n', fontsize = 20)

    ax.scatter(dates, closing_prices, facecolors='none', edgecolors='black', linewidth = 1, s = 80, label = 'Closing Prices')
    ax.plot(dates, smoothed_prices, color = 'red', linestyle = '--', linewidth = 4, label = 'Smoother')
    ax.plot(dates, closing_prices, color = 'dodgerblue', linewidth = 1, alpha = 1, label = 'Actual')

    ax.grid(which = 'major')
    plt.legend(loc = 2, fontsize = 18)
    plt.show()


#!/usr/bin/env python
#Plot a histogram
import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns(df):
    # Compute and return the daily values.  
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns

def test_run():
    # Read data
    dates = pd.date_range('2012-09-05', '2012-09-12')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)
    
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns", xlabel="Date")

    # Plot a histogram
    daily_returns.hist(bins=20)    #default number of bins is 10, changing the number of bins to 20
    # Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print "mean=", mean
    std = daily_returns['SPY'].std()
    print "std=", std

    # Add the mean to the graph
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    #For standard deviation we want plus and minus standard deviation so do it twice
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

    plt.show()

    # Compute kurtosis
    print "Kurtosis, if positive it's a fat tail with lots of outliers:"
    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()

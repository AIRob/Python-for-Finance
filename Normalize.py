#!/usr/bin/env python
'''
While I followed along with the syntax in lectures it isn't working in mine. =(
'''
import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """ Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:    # add SPY for referece, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                    parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY': # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

#This is the code to normalize the data
def normalize_data(df):
    """ Normalize stock prices using the first row of the dataframe.
        df.ix[0, :] gives us the first row, all stocks start with price 1.0 now
    """
    return df / df.ix[0,:]

def plot_data(df, title="Stock prices"):
    # Plot stock prices
    # title determines what the title of the graph will be
    # By setting up an "ax" or axis variable we can set labels
    # fontsize can make the graph more readable
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()  # Must be called to show plots in some environments

def test_run():
     # Define a date range
    dates = pd.date_range('2012-09-06', '2012-09-11')
    # Choose stock symbols to read
    symbols = ['IBM', 'AAPL']
    # Get stock data    
    df = get_data(symbols, dates)
    print df
    normalized = normalize_data(df)
    plot_data(normalized)

if __name__ == "__main__":
    test_run()

#!/usr/bin/env python
import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                                parse_dates = True, usecols=['Date', 'Adj Close']
                                                    , na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp, how='inner')
        if symbol == 'SPY': #Drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
    
    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2012-09-06', '2012-09-12')

    # Choose stock symbols to read
    symbols = ['IBM', 'AAPL', 'GOOG', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    df = df[::-1] #Reverses a list, is necessary b/c the list is ordered backwards
    
    #IMPORTANT STUFF, various types of slicing
    print df.ix['2012-09-05':'2012-09-11']  #Row Slicing
    print("Google:")
    print df['GOOG']    #Column slicing grabs single column
    print df[['IBM', 'GLD']]    # a list of labels selects multiple columns
    print df.ix['2012-09-07':'2012-09-11', ['SPY', 'IBM']]  # Slice by row and column

if __name__ == "__main__":
    test_run()

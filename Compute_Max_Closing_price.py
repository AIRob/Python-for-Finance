#!/usr/bin/env python

import pandas as pd

def get_max_close(symbol):
    """Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) #Read in data
    return df['Close'].max() #Compute and return max

def test_run():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Max close"
        print symbol
        print get_max_close(symbol)

if __name__ == "__main__":  # if run standalone
    test_run()

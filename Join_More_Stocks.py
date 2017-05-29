#!/usr/bin/env python
import pandas as pd

def test_run():
    #Define date range
    start_date = '2012-09-06'
    end_date = '2012-09-11'
    dates = pd.date_range(start_date, end_date)

    #Create an empty dataframe
    df1 = pd.DataFrame(index = dates)

    # Read SPY data into temporary dataframe
    # If we don't specify index_col then it defaults to the 0, 1, 2, generated
    # indices which means the joins will be empty
    # parse_dates converts the strings of dates into datetime objects
    # usecols parameter removes all columns except the ones we specify/want/need
    # na_values converts strings that say "nan" to Not a Number / NaN
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", 
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    #Rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # Do an inner join so only rows that exist in both are added
    df1 = df1.join(dfSPY, how='inner')

    #Read in more stocks
    symbols = ['AAPL', 'IBM']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date','Adj Close']
                                                ,na_values=['nan'])
        #Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp) # Use default how='left'
    
    print df1

if __name__ == '__main__':
    test_run()

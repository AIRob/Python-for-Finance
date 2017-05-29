#!/usr/bin/env python
''' Build a dataframe in pandas '''
import pandas as pd

def test_run():
    #Create a data range of DatetimeIndex
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    #Create a dataframe/csv with the index being dates instead of 0,1,2..etc
    df1 = pd.DataFrame(index=dates)
    print df1

if __name__ == "__main__":
    test_run()

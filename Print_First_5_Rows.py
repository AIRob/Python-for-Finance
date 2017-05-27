#!/usr/bin/env python
# Print the first 5 rows of a csv file
# Taken from lectures of Maching Learning for Trading
import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df.head() #print entire dataframe

if __name__ == "__main__":
    test_run()

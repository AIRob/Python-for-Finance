#!/usr/bin/env python
# Example taken from Machine Learning for Trading lecture

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df    #print entire dataframe

if __name__ == "__main__":
    test_run()

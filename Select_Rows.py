#!/usr/bin/env python

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df[2:4] #rows between index 2 and 3

if __name__ == "__main__":
    test_run()

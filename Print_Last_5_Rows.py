#!/usr/bin/env python
# Print last 5 rows of a csv

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df.tail()

if __name__ == "__main__":
    test_run()

#!/usr/bin/env python
# Creating NumPy arrays
import numpy as np

def test_run():
    # Empty array, doesn't mean zeroes, will have random crap from RAM
    print np.empty(5)
    print np.empty((5, 4))
    # Array of 1s
    print np.ones((5, 4))
    # specify the datatype so it's not just floats
    print np.ones((5, 4), dtype=np.int_)

if __name__ == "__main__":
    test_run()

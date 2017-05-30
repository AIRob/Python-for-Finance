#!/usr/bin/env python
import numpy as np

def test_run():
    a = np.random.random((5, 4))    # 5 x 4 array of random numbers
    print a
    print a.shape   #Gives you shape/dimensions of array
    print a.shape[0]    #Return number of rows
    print a.shape[1]    #Return number of columns
    print a.size        #Return number of elements, 20 in this case
    print a.dtype       #Get the datatype

if __name__ == "__main__":
    test_run()

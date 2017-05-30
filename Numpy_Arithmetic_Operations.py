#!/usr/bin/env python
# Arithmetic operations
import numpy as np

def test_run():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print "Original array a:\n", a

    # Multiply a by 2
    # When you multiply an array a new one is created and old one is unchanged
    print "\nMultiply a by 2:\n", 2 * a

    # Divide a by 2, integer division
    print "\nDivide a by 2:\n", a / 2

    # Divide a by 2.0, float division
    print "\nDivide a by 2.0:\n", a / 2.0

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print "Original array a:\n", a
    print "Original array b:\n", b
    # Add the two arrays
    print "\nAdd a + b:\n", a + b
    # Multiply the two arrays, does element by element multiplication rather than dog product or whatever
    print "\nMultiply a and b:\n", a * b    
    # Divide a by b, integer division
    print "\nDivide a by b:\n", a / b


if __name__ == "__main__":
    test_run()

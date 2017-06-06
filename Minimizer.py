#!/usr/bin/env python
# Minimize an objective function, using SciPy.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    # Given a scalar X, return some value (a real number)
    Y = (X - 1.5)**2 + 0.5
    print "X = {}, Y = {}".format(X, Y) #for tracing
    return Y

def test_run():
    Xguess = 2.0
    '''
    f is our guess
    Xguess is the initial guess
    the method is a specific algorithm
    disp being true means that it will be verbose about what it discovers
    '''
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
    print "Minima found at:"
    print "X = {}, Y = {}".format(min_result.x, min_result.fun)

    # Plot function values, mark Minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()

if __name__ == "__main__":
    test_run()

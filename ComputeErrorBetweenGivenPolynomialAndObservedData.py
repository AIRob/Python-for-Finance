import numpy as np

def error_poly(C, data):
    ''' Compute error between given polynomial and observed data.

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficient
    data: 2D array where each row is a point (x, y)

    Returns error as a single real value.
    '''
    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err

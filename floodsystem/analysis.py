import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """
    This function computes a least-squares fit of a polynomial of degree p to water level data.
    """
    x = matplotlib.dates.date2num(dates)
    polynomial_shifted = np.polyfit(x-x[0],levels,p)
    # Some stations have corrupt data which affect data structure conversion in polyfit
    return None, None
    #1d array shifted
    poly = np.poly1d(polynomial_shifted)
    #print(len(polynomial_shifted))
    #print(len(poly))
    d0 = x[0]
    #print(poly)
    return poly, d0

import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    #1d array shifted
    polynomial_shifted = np.polyfit(x-x[0],levels,p)
    poly = np.poly1d(polynomial_shifted)
    #print(len(polynomial_shifted))
    #print(len(poly))
    d0 = x[0]
    #print(poly)
    return poly, d0

import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    d0 = 0
    date_list = []

    #shifting each value
    for i in range (len(x)):
        shifted_value = x[i] - d0
        date_list.append(shifted_value)

    #1d array shifted
    polynomial_shifted = np.polyfit(date_list,levels,p)
    poly = np.poly1d(polynomial_shifted)

    return poly, d0

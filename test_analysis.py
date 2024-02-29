from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy as np

def test_polyfit():
    dates = ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05"]
    levels = [1.0, 2.0, 3.0, 4.0, 5.0]
    degree = 2

    # Call the function to get the result
    poly, d0 = polyfit(dates, levels, degree)

    # Check the correctness of the result
    assert isinstance(poly, np.poly1d)
    assert isinstance(d0, float)
    poly, date_shift = polyfit(dates, levels, 3)
    assert poly is not None and date_shift is not None
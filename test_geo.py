"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import random
from decimal import Decimal, getcontext


def test_stations_by_distance():
    """Testing that the input coordinates is a tuple, the output is arranged in distance"""

    #Generating random test coordinates
    getcontext().prec = 15
    test_coordinates = (Decimal(random.uniform(-90,90)),Decimal(random.uniform(-180,180)))

    #run function
    final = stations_by_distance(build_station_list(),test_coordinates)

    #Testing results
    assert isinstance(test_coordinates, tuple)
    assert all(final[i][1] <= final[i + 1][1] for i in range(len(final) - 1))
    assert final[-1][1] == max(station[1] for station in final)
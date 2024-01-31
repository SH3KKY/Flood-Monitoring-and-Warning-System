"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import random
import haversine
from decimal import Decimal, getcontext

def test_stations_by_distance():
    """Testing that the input coordinates is a tuple, the output is arranged in distance"""
    #Generating random test coordinates
    getcontext().prec = 15
    test_coordinates = (Decimal(random.uniform(-90,90)),Decimal(random.uniform(-180,180)))
    all_stations = build_station_list()

    #run function
    distance_result = stations_by_distance(all_stations,test_coordinates)

    #Testing results
    assert isinstance(test_coordinates, tuple)
    assert all(distance_result[i][1] <= distance_result[i + 1][1] for i in range(len(distance_result) - 1))
    assert distance_result[-1][1] == max(station[1] for station in distance_result)

def test_stations_within_radius():
    """Testing whether the function correctly determines whether stations are within specified radii of an origin (being Cambridge Centre)"""
    all_stations = build_station_list()
    test_radius = random.randint(0,50)
    origin = (52.2053, 0.1218)
    radius_result = stations_within_radius(all_stations,origin,test_radius)
    
    if test_radius == 0:
        assert len(radius_result) == 0 
    else:
        for station in all_stations:
            if station.name in radius_result:
                print(haversine.haversine(origin,station.coord))
                #print(station.name)
                #print(test_radius)
                assert haversine.haversine(origin,station.coord) < test_radius
    

test_stations_within_radius()
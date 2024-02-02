"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
import random
import haversine
from decimal import Decimal, getcontext

'''###################Test for task 1B########################'''

def test_stations_by_distance():
    """
    Testing that the outputs are the correct data type
    and the output is arranged in ascending distance
        
    """

    test_coordinates = (52.2053, 0.1218)
    all_stations = build_station_list()
    distance_result = stations_by_distance(all_stations,test_coordinates)

    #Testing data types
    assert isinstance(test_coordinates, tuple)
    assert isinstance(distance_result, list)
    for index in range(0,len(distance_result)-1):
        assert isinstance(distance_result[index], tuple)
        assert isinstance(distance_result[index][0],str)
        assert isinstance(distance_result[index][1],float)

    #Testing for specific value
    assert distance_result[10][0] == "Lode"
    assert distance_result [10][1] == 9.067126157017764

    #Testing list is arranged in distance
    assert all(distance_result[i][1] <= distance_result[i + 1][1] for i in range(len(distance_result) - 1))
    assert distance_result[-1][1] == max(station[1] for station in distance_result)

#test_stations_by_distance()
'''###################Test for task 1C########################'''

def test_stations_within_radius():
    """

    Testing whether the outputs are the correct data type 
    and function correctly determines whether stations are 
    within specified radii of an origin (being Cambridge Centre)

    """
    
    all_stations = build_station_list()
    test_radius = 15
    origin = (52.2053, 0.1218)
    radius_result = stations_within_radius(all_stations,origin,test_radius)

    #Testing data types
    assert isinstance(radius_result, list)
    for index in range(0,len(radius_result)-1):
        assert isinstance(radius_result[index],str)

    #Testing the number of stations within the specified test radius
    assert len(radius_result) == 14

    #Testing that the distance between the origin and station is less than the specified test radius
    if test_radius == 0:
        assert len(radius_result) == 0 
    else:
        for station in radius_result:
            if station in all_stations:
                #print(haversine.haversine(origin,station.coord))
                #print(station.name)
                #print(test_radius)
                assert haversine.haversine(origin,station.coord) < test_radius
    

#test_stations_within_radius()

'''###################Test for task 1D########################'''     

def test_rivers_with_station():
    all_stations = build_station_list()
    river_set_result = rivers_with_station(all_stations)
    
    #Test for data types
    assert isinstance(river_set_result, set)
    for index in range(len(river_set_result)):
        assert isinstance((list(river_set_result))[index],str)
    


#test_rivers_with_station()

def test_stations_by_river():
    all_stations = build_station_list()
    river_dictionary_result = stations_by_river(all_stations)

    #Test for dictionary as output
    assert isinstance(river_dictionary_result, dict)



test_stations_by_river()

'''###################Test for task 1E########################'''



def test_rivers_by_station_number():
    all_stations = build_station_list()
    N = random.randint(0,21)
    dict_result = rivers_by_station_number(all_stations,N)
    assert isinstance(dict_result, list)
    for word in dict_result:
        assert isinstance(word, tuple)
    assert all(dict_result[i+1][1] <= dict_result[i][1] for i in range(len(dict_result) - 1))

'''will test that data type is list and individual data types are tuples'''

test_rivers_by_station_number()
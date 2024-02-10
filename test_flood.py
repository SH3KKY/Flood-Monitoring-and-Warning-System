from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

station1 = MonitoringStation("abcd","abcd","abcd",(0.1,0.1), (3,5), "River X", "X-Ville")
station2 = MonitoringStation("efgh","efgh","efgh",(0.2,0.2),None,"River Y", "Y-ville" )
station3 = MonitoringStation("ijkl","ijkl","ijkl",(0.3,0.3),(2,3),"River Z", "Z-ville" )
station4 = MonitoringStation("mnop","mnop","mnop",(0.3,0.3),(8,9),"River A", "A-ville" )
station5 = MonitoringStation("qrst","qrst","qrst",(0.3,0.3),(7,9),"River B", "B-ville" )

station1.latest_level = 25
station2.latest_level = 5
station3.latest_level = 9
station4.latest_level = -2
station5.latest_level = 20

'''###################Test for task 2B########################'''

def test_stations_level_over_threshold():
    """
    This function tests whether a list of tuples is printed,
    that the first and last values are correct
    that the output is in descending order
    and the output contains the correct number of tuples
    """

    stations = [station1,station2,station3,station4,station5]
    N = 5
    test_output = stations_level_over_threshold(stations, N)

    #print(test_output)

    assert isinstance(test_output, list) #checks if data structure is a list
    assert isinstance(test_output[0], tuple) # checks if data type of each element is a typle
    assert test_output[0] == (stations[0], 11) #check first tuple
    assert test_output[-1] == (stations[4],6.5) #check last tuple
    assert all(test_output[i][1] >= test_output[i + 1][1] for i in range(len(test_output) - 1)) #checks if in descending order
    assert len(test_output) == 3 #checks length
    assert all(i[1] > N for i in test_output) #checks all values are larger than tolerance

'''###################Test for task 2C########################'''

def test_stations_highest_rel_level():
    """
    This function tests whether a list is printed,
    the length of the list is equal to the number of stations requested
    and the list is in descending order
    """
    stations = [station1,station2,station3,station4,station5]
    N = 2
    out = stations_highest_rel_level(stations,N)

    assert isinstance(out, list) #checks if data structure is a list
    assert len(out) == N #checks if the length of the list is what is inputed
    assert all(out[i][1] >= out[i + 1][1] for i in range(len(out) - 1)) #checks if in descending order

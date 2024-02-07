from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels


stations = build_station_list()

tolerance = 0.8

update_water_levels(stations)

list_of_tuples = stations_level_over_threshold(stations, tolerance)

for i in range(0, len(list_of_tuples)):
    print(list_of_tuples[i][0], list_of_tuples[i][1])

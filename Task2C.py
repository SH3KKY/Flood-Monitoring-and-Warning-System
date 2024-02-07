from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels

N = 10

stations = build_station_list()

# for this exercise, i will assume that if the relative water level is below the low typical value the station is not at risk
# so if the relative water level is below 0, it will not be included in data used for the algorithm

update_water_levels(stations)

output = stations_level_over_threshold(stations, 0)
#print(output)

for i in range(1,N+1):
    print(output[-i][0], output[-i][1])
    #print(i)
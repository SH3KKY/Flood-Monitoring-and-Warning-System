from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

N = 20

stations = build_station_list()
update_water_levels(stations)

# for this exercise, i will assume that if the relative water level is below the low typical value the station is not at risk
# so if the relative water level is below 0, it will not be included in data used for the algorithm

output = stations_highest_rel_level(stations, N)

for i in range(0, len(output)):
    print(output[i][0], output[i][1])

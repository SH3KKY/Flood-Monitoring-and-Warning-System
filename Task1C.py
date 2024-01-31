from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()
Cambridge_Centre = (52.2053, 0.1218)
radius = 10
run = stations_within_radius(stations,Cambridge_Centre,radius)
print(run)
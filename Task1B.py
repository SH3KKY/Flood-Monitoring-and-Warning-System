from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
new = stations_by_distance(build_station_list(),(52.2053, 0.1218))
print("The closest 10 stations to the specified coordinates:", new[:10])
print("The furthest 10 stations to the specified coordinates:", new[-10:])
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

days_back = 10

N = 5

output = stations_highest_rel_level(stations, N)

for item in output:
    levels, dates = fetch_measure_levels(
        item[0].measure_id, dt=datetime.timedelta(days=days_back))
    #print(levels,dates)
    #print(len(dates))
    #print(len(levels))
    plot_water_levels(item[0], dates, levels)


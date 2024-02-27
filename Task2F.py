from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()
update_water_levels(stations)

days_back = 2

N = 5
p = 4
output = stations_highest_rel_level(stations, N)

for item in output:
    dates, levels = fetch_measure_levels(
        item[0].measure_id, dt=datetime.timedelta(days=days_back))
    #print(levels, dates)
    #print(levels)
    plot_water_level_with_fit(item[0],dates, levels, p)
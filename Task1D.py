from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


river_keys = ['River Aire','River Cam','River Thames']    #this is the specific key

stations = build_station_list()

rivers_dictionary = (stations_by_river(stations))


output_stations = []
for i in range(len(river_keys)):
    temp_key = river_keys[i]
    output_stations = rivers_dictionary[temp_key]
    output_stations = sorted(output_stations)
    print(output_stations)
    output_stations = []
    print('\n')

all_rivers_with_streams = []

for stream in rivers_dictionary:
    if rivers_dictionary[stream] != []:
        all_rivers_with_streams.append(stream)
    
all_rivers_with_streams = sorted(all_rivers_with_streams)

number_of_stations = len(rivers_dictionary)

print(number_of_stations,'stations. First 10 - ',all_rivers_with_streams[0:9])

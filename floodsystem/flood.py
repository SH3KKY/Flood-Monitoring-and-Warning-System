def stations_level_over_threshold(stations, tol):

    out_of_tol = []
    
    for station in stations:
        if station.typical_range_consistent() and station.latest_level != None:
#            print(station.name, station.relative_water_level())
            if station.relative_water_level() > tol:
                out_of_tol.append((station.name,station.relative_water_level()))
        
    out_of_tol_sorted = sorted(out_of_tol, key = lambda x: x[1])
    return out_of_tol_sorted


def stations_highest_rel_level(stations, N):

    return_list = []

    output = stations_level_over_threshold(stations, 0)
    i = 0
    output.reverse()
    #print(output)
    while i < N:
        return_list.append(output[i])
        i+=1
    
    #print(return_list)

    return return_list

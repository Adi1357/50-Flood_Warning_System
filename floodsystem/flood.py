from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

#Task 1B:
def stations_level_over_threshold(stations, tol):
    level_over_thereshold_list= []
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
           level_over_thereshold_list.append((station, station.relative_water_level()))
           
    return level_over_thereshold_list

# Task 1C:
def stations_highest_rel_level(stations, N):
    list_of_stations_and_relative_levels = []
    for station in stations:
        if station.relative_water_level() is not None:
            list_of_stations_and_relative_levels.append((station, station.name, station.relative_water_level()))
    list_of_stations_and_relative_levels = sorted_by_key(list_of_stations_and_relative_levels, 2)
    stations_with_highest_relative_levels = []
    index = -1
    for i in range(N):
        stations_with_highest_relative_levels.append(list_of_stations_and_relative_levels[index][0])
        index -= 1
    #while -1 * index <= len(list_of_stations_and_relative_levels) and list_of_stations_and_relative_levels[index][1] == list_of_stations_and_relative_levels[index+1][1]:
        #stations_with_highest_relative_levels.append(list_of_stations_and_relative_levels[index])
        #index -= 1
    return stations_with_highest_relative_levels

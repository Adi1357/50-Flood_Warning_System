from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    level_over_thereshold_list= []
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
           level_over_thereshold_list.append((station, station.relative_water_level()))
           
    return level_over_thereshold_list


# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
##removed .utils as i was having problems importing the function
from utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from stationdata import build_station_list
from station import MonitoringStation
from collections import defaultdict


#Task 1B
def stations_by_distance(stations, p):
    distance = []

    
    for station in stations:
        distance.append((station.name,station.town, haversine(station.coord,p)))               
 
    return (sorted_by_key((distance),(2)))




#def stations_within_radius(stations, centre, r):


#Task 1D
def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return print(f"{len(rivers)} stations. First 10 - [{rivers[slice(10)]}]")

def stations_by_river(stations):
    ret = {}
    #for station in stations:
     #   if station.river in ret:
      #      ret[station.river].append(station.name)
       # else:
        #    ret[station.river] = [station.name]
  

    for station in stations:
        if station.river not in ret:
            ret[station.river] = [station.name]
        else:
            ret[station.river].append(station.name)
            ret[station.river].sort()
        
    

    return ret

stations= build_station_list()
station ={}

print(stations_by_river(stations)['River Aire'])


# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
##removed .utils as i was having problems importing the function
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from collections import defaultdict


#Task 1B
def stations_by_distance(stations, p):
    distance = []

    for station in stations:
        distance.append((station.name,station.town, haversine(station.coord,p)))               
 
    return (sorted_by_key((distance),(2)))


#Task 1C
def stations_within_radius(stations, centre, r):
    list_of_stations_in_radius = []
    
    for station in stations:
        if haversine(station.coord, centre) <= r:
            list_of_stations_in_radius.append(station)

    return [station.name for station in list_of_stations_in_radius]
    
#def stations_within_radius(stations, centre, r):


#Task 1D
def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers
    

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




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



def stations_by_distance(stations, p):
    distance = []

    
    for station in stations:
        distance.append((station.name,station.town, haversine(station.coord,p)))               
 
    return print(sorted_by_key((distance),(2)))


stations= build_station_list()
#stations_by_distance(stations, (52.2053, 0.1218))

#def stations_within_radius(stations, centre, r):
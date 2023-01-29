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


s=build_station_list()

def stations_by_distance( stations, p):
    return haversine(stations.coord, p) 

stations_by_distance(s, (2,3))
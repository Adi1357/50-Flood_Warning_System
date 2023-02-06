import sys
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations


stations = build_station_list()

def test_1B():
    assert len(stations_by_distance(stations, (1,1))) == len(stations)

def test_1C():
    assert len(stations_within_radius(stations, (0, 0), 40000)) == len(stations)

def test_1D():
    assert len(rivers_with_station(stations)) < len(stations)
    assert type(stations_by_river(stations)) == dict

def test_1E():
    assert len(rivers_by_station_number(stations, 9)) == 9

def test_1F():
    assert  len(inconsistent_typical_range_stations(stations)) <= len(stations)


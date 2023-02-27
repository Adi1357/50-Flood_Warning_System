import sys
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
from floodsystem.flood_warning import flood_warning_rel



stations = build_station_list()


    
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)


test_station_1 = MonitoringStation(station_id= "test_station_1", measure_id = "measure_station_1", label = "some station_1", coord= (1.0, 2.0), typical_range = (-2.3, 3.4445), river = "River 1", town= "My Town_1")
test_station_2 = MonitoringStation(station_id= "test_station_2", measure_id = "measure_station_2", label = "some station_2", coord= (2.0, 3.0), typical_range = (-12.3, 45.45), river = "River 2", town= "My Town_2")
test_station_3 = MonitoringStation(station_id= "test_station_3", measure_id = "measure_station_3", label = "some station_3", coord= (3.0, 4.0), typical_range = (-0.3, 4.5), river = "River 3", town= "My Town_3")
test_station_4 = MonitoringStation(station_id= "test_station_4", measure_id = "measure_station_4", label = "some station_4", coord= (4.0, 5.0), typical_range = (-1.3, 4.45), river = "River 4", town= "My Town_4")

test_station_1.latest_level = -2.3
test_station_2.latest_level = 3.3
test_station_3.latest_level = 5.3
test_station_4.latest_level = 6.3

test_station_5 = MonitoringStation(station_id= "test_station_5", measure_id = "measure_station_5", label = "some station_1", coord= (1.0, 2.1), typical_range = (-2.3, 3.4446), river = "River 1", town= "My Town_5")
test_station_6 = MonitoringStation(station_id= "test_station_6", measure_id = "measure_station_6", label = "some station_2", coord= (2.0, 3.1), typical_range = (-12.3, 45.46), river = "River 1", town= "My Town_6")
test_station_7 = MonitoringStation(station_id= "test_station_7", measure_id = "measure_station_7", label = "some station_3", coord= (3.0, 4.1), typical_range = (-0.3, 4.6), river = "River 1", town= "My Town_7")
test_station_8 = MonitoringStation(station_id= "test_station_8", measure_id = "measure_station_8", label = "some station_4", coord= (4.0, 5.1), typical_range = (-1.3, 4.46), river = "River 2", town= "My Town_8")


test_list= (test_station_1, test_station_2, test_station_3, test_station_4)
test_list_2= (test_station_1, test_station_2, test_station_3, test_station_4, test_station_5, test_station_6, test_station_7, test_station_8)

#Test 1B
def test_stations_by_distance():
    test_list_1B = stations_by_distance(test_list, (1,1))
    assert test_list_1B[0][0:2] == ("some station_1","My Town_1")
    assert test_list_1B[1][0:2] == ("some station_2","My Town_2")
    assert test_list_1B[2][0:2] == ("some station_3","My Town_3")

#Test 1C
def test_stations_within_radius():
    #One latitude and longitude degree is approximately 120km near the equator
    test_list_1C_a = stations_within_radius(test_list, (0.0, 1.0), 2*120)
    test_list_1C_b = stations_within_radius(test_list, (0.0, 1.0), 3*120)
    test_list_1C_c = stations_within_radius(test_list, (0.0, 1.0), 4*120)
    assert len(test_list_1C_a) == 1
    assert len(test_list_1C_b) == 2
    assert len(test_list_1C_c) == 3

    #Further assertion of validity of actual data
    assert len(stations_within_radius(stations, (0, 0), 40000)) == len(stations)

#Test 1D
def test_rivers_with_station():
    test_rivers_list = rivers_with_station(test_list)
    assert test_rivers_list == ['River 1', 'River 2', 'River 3', 'River 4']

def test_stations_by_river():
    test_dic= stations_by_river(test_list)
    assert test_dic['River 1'] == ['some station_1']
    assert test_dic['River 2'] == ['some station_2']
    assert test_dic['River 3'] == ['some station_3']

#Test 1E
def test_rivers_by_station_number():
    test_list_1E = rivers_by_station_number(test_list_2, 3)
    assert test_list_1E[0] == ('River 1', 4)
    assert test_list_1E[1] == ('River 2', 2)
    assert ('River 3', 1) in test_list_1E[2:] 
    assert ('River 4', 1) in test_list_1E[2:] 

    #Further assertion of validity of actual data
    for n in range(5):
        assert len(rivers_by_station_number(stations, n)) >= n 


#Test 1F
def test_inconsistent_typical_range_stations():
    test_inconsistentx_list = inconsistent_typical_range_stations(test_list)
    assert test_inconsistentx_list == []

#Test 2B
def test_stations_level_over_threshold():
    test_list_over_list = stations_level_over_threshold(test_list, 7)
    assert test_list_over_list == []

#Test 2E
def test_plot_water_levels():
    assert plot_water_levels(test_station_1,10) is ValueError





    

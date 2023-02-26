from floodsystem.flood_warning import flood_warning  
from floodsystem.flood_warning import flood_warning_rel
from floodsystem.flood_warning import consistent
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    severe_risk_list = []
    consistent_stations = consistent(stations, 10)

    for station in consistent_stations:
        if station.typical_range_consistent() == True:
            if flood_warning(station,10) > 0.5 and flood_warning_rel(station,10) == 'Severe risk':
                severe_risk_list.append(station.name)

            elif flood_warning(station,10) >= 0.01 and flood_warning_rel(station,10) == 'High risk':
                pass
                #print(station.name, "High Risk")
    
            elif flood_warning(station,10) >= 0.0 and flood_warning_rel(station,10) == 'Moderate risk':
                pass
                #print(station.name, "Moderate Risk")
        
            else:
                pass
                #print(station.name, "Low Risk")

    print(severe_risk_list)


    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
    
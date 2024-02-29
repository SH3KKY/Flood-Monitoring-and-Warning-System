import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num
from floodsystem.flood import stations_level_over_threshold
import datetime

#Initialise risk categories

severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []
unknown = [] #for stations with invalid data
rising = []
falling = []
stations = build_station_list()
update_water_levels(stations)

def risk_assessment(station):
    
    one_day_dates, one_day_levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))
    #two_day_dates, two_day_levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))

    invalid = False

    # Check if data is valid
    if station.typical_range is not None and station.latest_level is not None and len(station.typical_range) == 2:
        low = station.typical_range[0]
        high = station.typical_range[1]
    else:
        unknown.append(station.town)
        invalid = True

    if not invalid:
        latest = (station.latest_level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
        # Assessing the immediate risk
        if len(one_day_dates) != 0:
            if latest >= 1:
                severe_risk.append(station.town)
            elif latest >= 0.7:
                high_risk.append(station.town)
            elif latest>= 0.4:
                moderate_risk.append(station.town)
            elif latest >= 0:
                low_risk.append(station.town)
        else:
            unknown.append(station.town)
            invalid = True
        """
        if not invalid:
            #print(one_day_dates)
            # Assess whether the water level is going to rise or fall
            poly, d0 = polyfit(one_day_dates, one_day_levels, 3)
            if poly ==  None and d0 == None:
             unknown.append(station.town)
            else:
                future = poly(max(date2num(one_day_dates) - d0))
                future_level = (future - low) / (high - low)
                if future_level > station.latest_level:
                    rising.append(station.town)
                else:
                    falling.append(station.town)
        """

for station in stations:
    risk_assessment(station)
    risk = None
    trend = None
    #print(station.town)
    if station.town in severe_risk:
        risk = "\033[91mVery High Risk\033[0m"  #Red 
    elif station.town in high_risk:
        risk = "\033[93mHigh Risk\033[0m"  # yellow 
    elif station.town in moderate_risk:
        risk = "\033[94mModerate Risk\033[0m"  #Blue 
    elif station.town in low_risk:
        risk = "\033[92mLow Risk\033[0m"  #Green 
    """
    if station.town in rising:
        trend = "\033[91mRising\033[0m"  #Red 
    elif station.town in falling:
        trend = "\033[92mFalling\033[0m"  #Green 
    """
    if risk is not None:
        print(f"{station.town} is currently at {risk}.")
    else:
        print(f"No valid data available for {station.town}.")

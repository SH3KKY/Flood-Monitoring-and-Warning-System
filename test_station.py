# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

'''###################Test for task 1F########################'''

#3 cases: station is fine, station has no data, station have high value<low value
station1 = MonitoringStation("abcd","abcd","abcd",(0.1,0.1), (0.3,0.2), "River X", "X-Ville")
station2 = MonitoringStation("efgh","efgh","efgh",(0.2,0.2),None,"River Y", "Y-ville" )
station3 = MonitoringStation("ijkl","ijkl","ijkl",(0.3,0.3),(0.2,0.3),"River Z", "Z-ville" )

def test_typical_range_consistent():
    """Test whether consistent data is detected for known test cases"""
    assert station1.typical_range_consistent() == False
    assert station2.typical_range_consistent() == False
    assert station3.typical_range_consistent() == True

def test_inconsistent_typical_range_stations():
    """Test whether inconsistent data is produced for known test cases"""
    assert len(inconsistent_typical_range_stations([station1])) > 0 
    assert len(inconsistent_typical_range_stations([station2])) > 0
    assert len(inconsistent_typical_range_stations([station3])) == 0

test_typical_range_consistent()
test_inconsistent_typical_range_stations()
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import haversine

def stations_by_distance(stations, p):
   """This function calculates the distance between provided stations and a provided coordinate."""
   point_to_station_dist = [] #Initialise list
   for station in stations:
      #print(station.coord)
      distance = haversine.haversine(p,station.coord)
      temp = (station.name, distance)
      point_to_station_dist.append(temp)
   point_to_station_dist = sorted_by_key(point_to_station_dist,1)
   return point_to_station_dist

    
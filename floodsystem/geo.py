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
   return sorted_by_key(point_to_station_dist,1)
   

   '''################Task 1C################'''


def stations_within_radius(stations, centre, r):
   """This function lists the stations within a radius of a provided coordinate"""
   within_radius = []

   """this code simply iterates through the stations, calculates the distance, and compares it with the input radius"""
   for station in stations:
      distance = haversine.haversine(centre,station.coord)
      if distance < r:
         #print(distance)
         within_radius.append(station.name)

   return sorted(within_radius)


   '''################Task 1D################'''


def rivers_with_station(stations):

   '''this function forms a set of all the river names to be used in stations_by_river'''

   all_the_rivers = []

   for station in stations:
      all_the_rivers.append(station.river)

   all_river_set = set(all_the_rivers)

   return all_river_set


def stations_by_river(stations):
   '''this function forms a dictionary of the key: river name to the value: station name'''
   
   rivers_to_stations = {}

   all_rivers = rivers_with_station(stations) #this calls the previous function and stores the set with all the river names

   stations_on_river = [] #for each river we will update this and store the stations on that river, add that to the dictionary as a value, the clear the list

   for stream in all_rivers:
      for station in stations:
         if station.river == stream:
            stations_on_river.append(station.name)

   
      #print(stream, stations_on_river)
      rivers_to_stations[stream] = stations_on_river


      stations_on_river = []
   
   return rivers_to_stations


   '''################Task 1E################'''


def rivers_by_station_number(stations, N):

   '''This first section of the function creates a dictionary of each river to the number of stations on it'''

   river_to_number = {}
   
   rivers_to_stations = stations_by_river(stations)

   #print(rivers_to_stations)


   for river in rivers_to_stations:
      #print(rivers_to_stations[river])
      river_to_number[river] = len(rivers_to_stations[river])

   '''This next section creates a set with all the stations_on_river numbers'''

   all_the_numbers = []

   for river in river_to_number:
      all_the_numbers.append(river_to_number[river])

   all_the_numbers_set = sorted(set(all_the_numbers))

   #return(all_the_numbers_set)

   '''This final section uses N and all_the_numbers_set to return the rivers with the N top monitoring stations'''

   for i in range(0,N):
      station_number_value = all_the_numbers_set[len(all_the_numbers_set)-i-1]
      print(station_number_value)
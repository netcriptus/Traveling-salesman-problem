#!/usr/bin/python

from sys import stdin
from math import sqrt
from itertools import permutations

import functools


class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""
      return functools.partial(self.__call__, obj)



class Salesman(object):
    def __init__(self, number_of_cities):
        self.number_of_cities = number_of_cities
        self.roadmap = None
        self.cities = []
        self.city_indexes = [i+1 for i in range(number_of_cities-1)]
        self.current_city = 0

    def getCities(self):
        for i in range(self.number_of_cities):
            city = stdin.readline()
            city = city.strip().split(" ")
            self.cities.append((int(city[0]),
                                int(city[1])))


    def mountMap(self):
        self.roadmap = [[] for i in range(self.number_of_cities)]
        for i in range(self.number_of_cities-1):
            for j in range(i, self.number_of_cities):
                distance = self.__reckonDistance(self.cities[i], self.cities[j])
                self.roadmap[i].append(distance)
                if i != j:
                    self.roadmap[j].append(distance)
        self.roadmap[-1].append(0.0)

    def __reckonDistance(self, city1, city2):
        distance = sqrt(pow(city1[0] - city2[0], 2) + pow(city1[1] - city2[1], 2))
        return distance
        
    def __totalDistance(self, tour):
      distance = 0
      for last_city, city in zip(tour[:-1], tour[1:]):
        distance += self.roadmap[last_city][city]
      return distance

    def nextCity(self, remaining_cities):
        return self.closestCity(self.current_city, remaining_cities)

    def closestCity(self, city, options):
        closest = options[0]
        shortest_distance = self.roadmap[city][options[0]]

        for option in options[1::]:
            if self.roadmap[city][option] < shortest_distance:
                shortest_distance = self.roadmap[city][option]
                closest = option

        return closest

    @memoized
    def shortestTour(self, cities):
      shortest_length = self.__totalDistance([0] + cities + [0])
      best_tour = [0] + cities + [0]
      for solution in permutations(cities):
        length = self.__totalDistance([0] + list(solution) + [0])
        if length < shortest_length:
          shortest_length = length
          best_tour = [0] + list(solution)
      return best_tour, shortest_length
        
    def travel(self):
        tour, distance = self.shortestTour(self.city_indexes)
        norm_tour = [i+1 for i in tour]
        return norm_tour, distance

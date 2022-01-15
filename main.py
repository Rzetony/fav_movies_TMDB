# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:07:00 2022

This is my first python project, to learn and test:
- API, OOP, Saving to file, SQL - some features are not yet implemented

Version 1.0
Main function calls to create connection to TMDB API and get results of movie
with id that we pass. Movie object is created, its variables is data passed by
the API - title, release date, score, etc


@author: Rzetony
"""

# Importing module to connect to the API
import connection_cls as conct

# New connection object for id 550
# __init__ also creates movie object holding the data
connection = conct.connection_cls(550)

# Extracting movie object
movie = connection.pass_movie()

# Printing the keys of data dictionary
movie.print_options()

# Example of data we can access
print(f"{movie.title} budget was {movie.budget}$")


# Printing the title and users score
print(movie.title)
movie.print_score()
print("---------------")



"""
Example how to print a few movies in succesion.
Some basic error proofing is done if id leads nowhere


for i in range(10):
      connection = conct.connection_cls(550+i)
      movie = connection.pass_movie()
      if(type(movie) == type(0)):
          print("Wrong movie id")
      else:        
          print(movie.title)
          movie.print_score()
          print("---------------")

"""









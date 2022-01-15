# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:45:20 2022

This class sends requests to TMDB API asking for movie data.
NOT WORKING, KEY value is Auth key and I removed it for safety.
It will be expanded with more methods to search for movies, etc.


Version 1.0 
- Ability to ask for movie based on ID
- Creating movie_cls object to store results

@author: Rzetony
"""

# module to talk send http requests
import requests

# module with movie class - objects holding the data
import movie_cls as mvcls


class connection_cls:
    
    # Pass the Auth key as "?api_key=XX" where XX is your personal key
    KEY = "?api_key="
    
    # Basic url for GET requests for movie of specific id
    REQUEST ="https://api.themoviedb.org/3/movie/"
    
    
    # Constructor, id passed is movie id on TMDB
    def __init__(self, id):
        
        
        self.id = id
        
        # Assign data from TMDB
        movie_dict = self.get_movie()
        
        # Error check, is the movie_dict 0? then dont create movie object
        if(movie_dict == 0):
            self.movie = None
        else:
            # Create movie object with the dictionary as input
            self.movie = mvcls.movie_cls(movie_dict)
        
        
    # Send request for movie data of specific id    
    def get_movie(self):
        
        # Example https://api.themoviedb.org/3/movie/550?api_key=XX
        url = self.REQUEST + str(self.id) + self.KEY
                  
        response = requests.get(url)
      
        # Error check, status 200 is correct request
        if(response.status_code != 200)    :            
            # Returning 0 instead of the data dictionary
            return 0
        
        else:       
            # Converting the response to json and returning
            return response.json()
        

    # Method to pass the movie object (holding data) to main function
    def pass_movie(self):
        # Error check if movie is object or not created at all
        if(self.movie == None):
            return 0
        else:
            return self.movie
       

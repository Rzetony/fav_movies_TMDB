# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:53:29 2022

Class designed to hold data passed by TMDB API

Version 1.0
- gets dictionary of results from API and assigns it to the variables
- variables are accesible, to be used in next program Versions


@author: Rzetony
"""

class movie_cls:
    
    
    # Constructor assigns variables from dictionary
    def __init__(self, results_dict):
        
        # Dictionary with the data
        self.results_holder = results_dict
        
        # Not done as a loop to have explicit names of variables
        # Also this is constant as passed from TMDB API
        self.adult = results_dict["adult"]
        self.backdrop_path = results_dict["backdrop_path"]
        self.belongs_to_collection = results_dict["belongs_to_collection"]
        self.budget = results_dict["budget"]
        self.genres = results_dict["genres"]
        self.homepage = results_dict["homepage"]
        self.id = results_dict["id"]
        self.imdb_id = results_dict["imdb_id"]
        self.original_language = results_dict["original_language"]
        self.original_title = results_dict["original_title"]
        self.overview = results_dict["overview"]
        self.popularity = results_dict["popularity"]
        self.poster_path = results_dict["poster_path"]
        self.production_companies = results_dict["production_companies"]
        self.production_countries = results_dict["production_countries"]
        self.release_date = results_dict["release_date"]
        self.revenue = results_dict["revenue"]
        self.runtime = results_dict["runtime"]
        self.spoken_languages = results_dict["spoken_languages"]
        self.status = results_dict["status"]
        self.tagline = results_dict["tagline"]
        self.title = results_dict["title"]
        self.video = results_dict["video"]
        self.vote_average = results_dict["vote_average"]
        self.vote_count = results_dict["vote_count"]
        
                  
    # Print keys of the dictionary (Data categories)
    def print_options(self):
        
        print(self.results_holder.keys())
        
        # Alternative to print 1 by 1
        
        # for key in self.results_holder:
        #     print(key)
        
    
    # Print user score X /10 and with how many voters        
    def print_score(self):
        
        print(self.vote_average, "/ 10 after", self.vote_count, "votes")
            
            
            
            
# =============================================================================
#     dont need because its just as quick to acces the variables
#     
#     def get_title(self):
#         return self.title
#     
#     def get_id(self):
#         return self.id
#     
#     
# =============================================================================
    
            
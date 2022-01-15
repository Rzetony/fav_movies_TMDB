# fav_movies_TMDB
My first project in python to learn, as final form should work as favorite movie database, saving them (as data pulled from themoviedb.org) to a file on my local PC.

Version 1.0

Split program into main.py and 2 classes
- main.py where i call all the functions
- class connection_cls that will handle communication with TMDB API
- class movies_cls which will hold data that I get from TMDB API

To keep things simple in the first version I will only request data of single movie per request, based on id the movie has on themoviedb.org site.
Also the movie object will not have all the methods to access data.


Plans for future versions:
- Implement more requests in connection_cls ( search movies by parameter like release date, etc)
- Save the favorite movie data to a file / create a list of favorite movies in a file - learn SQL operations
- Create some simple GUI - show posters, then maybe implement buttons
- ... whatever I want to practice next
- Final goal is to have solid search based on scores and movie genres, then to show not released movies 


@Rzetony

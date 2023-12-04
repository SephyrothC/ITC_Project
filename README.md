# Movie Recommendation System

## Table of Contents
1. Overview
2. Implementation
3. User Interface
4. Future Work

## Overview <a name="overview"></a>

This project is a movie recommendation system built with Python and Flask. It uses data from the MovieLens dataset to recommend movies based on user input.

## Implementation <a name="implementation"></a>

The system is implemented as a Flask web application. The main part of the application is the `Movie` class, which represents a movie with attributes such as name, id, tags, link, and rating. The `MovieInit` function initializes the movies from a CSV file. The `load_average_ratings` function loads the average ratings for each movie from another CSV file.

The `get_movies_by_name` function takes a list of movie names and returns a list of `Movie` objects that have similar names. The `recommend_movies` function uses this list to find the most common genres among the movies, and then recommends other movies that have these genres and high ratings.

The application has a single route (`/`) that handles both GET and POST requests. If the request method is POST, the route function gets the movie names from the form data, finds the recommended movies, and displays them on the page. If the request method is not POST, the route function simply displays the home page without any movies.

## User Interface <a name="user-interface"></a>

The user interface is a simple web page with a form where the user can enter movie names. When the form is submitted, the page displays the recommended movies along with their ratings, tags, and a link to view the movie. If the user doesn't enter any movie names, an error message is displayed on the page.

## Future Work <a name="future-work"></a>

Currently, the system only uses movie names and genres to recommend movies. In the future, it could be improved to take into account other factors such as the user's past ratings, the popularity of the movies, and the ratings of similar users. Additionally, the user interface could be enhanced with features such as autocomplete for movie names, user accounts, and the ability to rate movies and save recommendations. 

This project is a great example of how you can use Python and Flask to build a simple but effective recommendation system. It demonstrates the power of data and algorithms in providing personalized experiences for users. Whether you're a movie buff looking for your next favorite film, or a developer seeking to learn more about recommendation systems, this project has something for you. Enjoy exploring it! 🎬🍿

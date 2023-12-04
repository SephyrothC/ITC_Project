import csv
from collections import Counter
from fuzzywuzzy import fuzz


def load_average_ratings():  # Function to load the average ratings
    with open('ml-25m/ml-25m/average.csv', 'r') as f:  # Open the average.csv file
        reader = csv.reader(f)  # Create a CSV reader
        next(reader)  # Skip the header row
        for row in reader:  # For each row in the CSV file
            movie_id = int(row[0])  # Get the movie id
            average_rating = float(row[1])  # Get the average rating
            # Add the average rating to the dictionary
            average_ratings[movie_id] = average_rating


average_ratings = {}  # Initialize the average ratings
load_average_ratings()  # Load the average ratings


class Movie:  # Define a class named Movie
    def __init__(self, id=0, name="", tags=None):  # Constructor for the Movie class
        self.name = name  # Assign the name
        self.id = id  # Assign the id
        self.tags = tags if tags is not None else []  # Assign the tags
        self.link = self.make_link()  # Create a link for the movie
        self.rating = self.get_average_rating()  # Get the average rating of the movie

    def make_link(self):  # Method to create a link for the movie on the MovieLens website
        return "https://movielens.org/movies/" + str(self.id)

    def get_average_rating(self):  # Method to get the average rating of the movie
        # Return the average rating for this movie
        return average_ratings.get(self.id, 0)

    def __str__(self):  # Method to return a string representation of the Movie object
        return f"Movie ID: {self.id}\nName: {self.name}\nRating: {self.rating}\nTags: {', '.join(self.tags)}\nLink: {self.link}\n\n"


def MovieInit():  # Function to initialize the movies
    movies = {}  # Initialize an empty dictionary to store the movies
    with open('ml-25m/ml-25m/movies.csv', 'r', encoding='utf-8') as f:  # Open the movies.csv file
        reader = csv.reader(f)  # Create a CSV reader
        next(reader)  # Skip the header row
        for row in reader:  # For each row in the CSV file
            id = int(row[0])  # Get the id
            name = row[1]  # Get the name
            tags = row[2].split('|')  # Split the genres string into a list
            # Create a Movie object and add it to the dictionary
            movies[id] = Movie(id, name, tags=tags)
    return movies  # Return the dictionary of movies


# Function to get movies by name
def get_movies_by_name(movie_names, movies_dict, limit=3):
    # Initialize an empty list to store the found movies
    found_movies = []
    # Iterate over the list of movie names
    for name in movie_names:
        # Iterate over the dictionary of movies
        for movie in movies_dict.values():
            # If the movie name is close enough to the searched name, add the Movie object to the list
            # You can adjust this threshold according to your needs
            if fuzz.ratio(movie.name, name) > 60:
                found_movies.append(movie)
    # Return the list of found movies
    return found_movies


def recommend_movies(movie_names, movies_dict, limit=5):  # Function to recommend movies
    # Find the most similar movie names in the movies_dict
    similar_movies = get_movies_by_name(movie_names, movies_dict)

    # Get the genres of the list of movies from the movies_dict
    genres = [movie.tags for movie in similar_movies]

    # Flatten the list of genres and get the three most common genres
    common_genres = Counter(
        [genre for sublist in genres for genre in sublist]).most_common(3)
    common_genres = [genre for genre, _ in common_genres]

    # Filter the movies_dict to only include movies with all common genres and sort by rating
    recommended_movies = sorted([movie for movie in movies_dict.values() if all(genre in movie.tags for genre in common_genres) and movie.id not in [
                                movie.id for movie in similar_movies]], key=lambda x: x.rating, reverse=True)

    # Return the top 5 movies
    return recommended_movies[:5]

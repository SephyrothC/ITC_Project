import requests
import csv
from collections import defaultdict, Counter
from fuzzywuzzy import process, fuzz
from flask import Flask, render_template

app = Flask(__name__, template_folder='../template')

# test


class Movie:
    def __init__(self, id=0, name="", tags=None):
        self.name = name
        self.id = id
        self.tags = tags if tags is not None else []
        self.link = self.make_link()
        self.rating = self.get_average_rating()

    def make_link(self):
        return "https://movielens.org/movies/" + str(self.id)

    def get_average_rating(self):
        # Retourner la note moyenne pour ce film
        return average_ratings.get(self.id, 0)

    def __str__(self):
        return f"Movie ID: {self.id}\nName: {self.name}\nRating: {self.rating}\nTags: {', '.join(self.tags)}\nLink: {self.link}\n\n"


def MovieInit():
    movies = {}
    with open('ml-25m/ml-25m/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            id = int(row[0])
            name = row[1]
            tags = row[2].split('|')  # Split the genres string into a list
            movies[id] = Movie(id, name, tags=tags)
    return movies


def load_average_ratings():
    with open('ml-25m/ml-25m/average.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            movie_id = int(row[0])
            average_rating = float(row[1])
            average_ratings[movie_id] = average_rating


def get_movies_by_name(movie_names, movies_dict, limit=3):
    # Initialiser une liste vide pour stocker les films trouvés
    found_movies = []
    # Parcourir la liste des noms de films
    for name in movie_names:
        # Parcourir le dictionnaire des films
        for movie in movies_dict.values():
            # Si le nom du film est suffisamment proche du nom recherché, ajouter l'objet Movie à la liste
            # Vous pouvez ajuster ce seuil en fonction de vos besoins
            if fuzz.ratio(movie.name, name) > 60:
                found_movies.append(movie)
    # Renvoyer la liste des films trouvés
    return found_movies


def recommend_movies(movie_names, movies_dict, limit=5):
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


def print_recommended_movies(recommended_movies):
    for movie in recommended_movies:
        print(movie)


@app.route('/')
def home():
    movies_dict = MovieInit()
    movie_names = ["Exorciste", "Saw", "Shinning"]
    recommended_movies = recommend_movies(movie_names, movies_dict)
    return render_template('index.html', movies=recommended_movies)


if __name__ == '__main__':
    average_ratings = {}
    load_average_ratings()
    app.run(debug=True)

    # movies_dict = MovieInit()
    # movie_names = ["Exorciste", "Saw", "Shinning"]
    # recommended_movies = recommend_movies(movie_names, movies_dict)

    # print_recommended_movies(recommended_movies)

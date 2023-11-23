import requests
import csv
from collections import defaultdict, Counter
from fuzzywuzzy import process, fuzz
from flask import Flask, render_template

app = Flask(__name__)


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
        return f"Movie ID: {self.id}\nName: {self.name}\nRating: {self.rating}\nTags: {', '.join(self.tags)}\nLink: {self.link}"


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


def recommend_movies(movie_names, movies_dict, limit=5):
    similar_movies = process.extractBests(
        ' '.join(movie_names), movies_dict.keys(), limit=limit)
    return [movies_dict[movie_id] for movie_id, _ in similar_movies]


@app.route('/')
def home():
    movies_dict = MovieInit()
    movie_names = ["Toy Story", "Nemo", "Hercule"]
    recommended_movies = recommend_movies(movie_names, movies_dict)
    return render_template('code/index.html', movies=recommended_movies)


if __name__ == '__main__':
    average_ratings = {}
    load_average_ratings()
    app.run(debug=True)

import csv
from collections import defaultdict


class Movie:
    def __init__(self, id=0, name="", rating=0, tags=None):
        self.name = name
        self.id = id
        self.rating = 0
        self.tags = tags if tags is not None else []
        self.link = self.make_link()

    def make_link(self):
        return "https://movielens.org/movies/" + str(self.id)

    def __str__(self):
        return f"Movie ID: {self.id}\nName: {self.name}\nRating: {self.rating}\nTags: {', '.join(self.tags)}\nLink: {self.link}"


def calculate_average_ratings():
    # Créer un dictionnaire pour stocker les notes de chaque film
    ratings = defaultdict(list)

    # Ouvrir le fichier CSV et lire les données
    with open('ml-25m/ml-25m/ratings.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            movie_id = int(row[1])
            rating = float(row[2])
            ratings[movie_id].append(rating)

    # Calculer la note moyenne pour chaque film
    average_ratings = {movie_id: sum(
        ratings_list) / len(ratings_list) for movie_id, ratings_list in ratings.items()}

    # Écrire les notes moyennes dans un nouveau fichier CSV
    with open('ml-25m/ml-25m/average.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['movieId', 'averageRating'])  # Write the header row
        for movie_id, average_rating in average_ratings.items():
            writer.writerow([movie_id, average_rating])


def MovieInit():
    movies = []

    # Ouvrir le fichier CSV et lire les données
    with open('ml-25m/ml-25m/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            id = int(row[0])
            name = row[1]
            tags = row[2].split('|')  # Split the genres string into a list
            movies.append(Movie(id, name, tags=tags))

    print(movies[27])


if __name__ == '__main__':
    calculate_average_ratings()
    MovieInit()

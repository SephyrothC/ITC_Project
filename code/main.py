import csv
from collections import defaultdict, Counter
from fuzzywuzzy import process, fuzz


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
    average_ratings = {movie_id: (sum(ratings_list) / len(ratings_list) if len(ratings_list) >= 1000 else 0.5)
                       for movie_id, ratings_list in ratings.items()}

    # Trier les notes moyennes par movieId
    sorted_ratings = sorted(average_ratings.items())

    # Écrire les notes moyennes dans un nouveau fichier CSV
    with open('ml-25m/ml-25m/average.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['movieId', 'averageRating'])  # Write the header row
        for movie_id, average_rating in sorted_ratings:
            writer.writerow([movie_id, average_rating])


def MovieInit():

    movies = {}

    # Ouvrir le fichier CSV et lire les données
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
    # Ouvrir le fichier CSV et lire les données
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


def search_movie(name, movies_dict, limit=3):
    # Créer une liste de noms de films à partir du dictionnaire de films
    movie_list = [movie.name for movie in movies_dict.values()]

    # Utiliser fuzzywuzzy pour trouver les films dont le nom est le plus proche de la chaîne donnée
    results = process.extract(name, movie_list, limit=limit)

    # Renvoyer les résultats
    return results


def search_movie_id_by_name(name, movies_dict):
    # Utiliser une compréhension de liste pour trouver l'ID du film correspondant
    movie_id = next((id for id, movie in movies_dict.items()
                    if movie.name.lower() == name.lower()), None)

    # Renvoyer l'ID du film trouvé ou None si aucun film n'a été trouvé
    return movie_id


def recommend_movies(movie_names, movies_dict, limit=5):

    # Trouver les films les plus similaires pour chaque nom dans movie_names
    similar_movies = get_movies_by_name(movie_names, movies_dict)

   # Récupérer les genres de ces films
    genres = [movie.tags for movie in similar_movies]

    # Compter le nombre d'occurrences de chaque genre
    genre_counts = Counter(
        genre for movie_genres in genres for genre in movie_genres)

    # Trouver les genres qui sont présents dans au moins deux des trois films
    common_genres = [genre for genre,
                     count in genre_counts.items() if count >= 2]

    same_genre_movies = [movie for movie in movies_dict.values() if len(
        set(movie.tags) & set(common_genres)) >= 2 and movie.rating != 5.0]

    # Trier ces films par note moyenne et prendre les cinq premiers
    top_movies = sorted(same_genre_movies,
                        key=lambda movie: movie.rating, reverse=True)[:limit]

    return top_movies


if __name__ == '__main__':
    # calculate_average_ratings()

    average_ratings = {}
    # Charger les notes moyennes au démarrage du programme
    load_average_ratings()

    # Initialiser la liste des films
    movies_dict = MovieInit()

    # Initialiser les noms des films pour lesquels vous voulez trouver des recommandations
    movie_names = ["Toy Story", "Nemo", "Hercule"]

    # Appeler la fonction recommend_movies pour obtenir les recommandations
    recommended_movies = recommend_movies(movie_names, movies_dict)

    # Afficher les films recommandés
    for movie in recommended_movies:
        print("\n================================\n")
        print(movie)

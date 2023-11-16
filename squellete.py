# Importation des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse.linalg import svds

# 1. Collecte de données
# Charger les données à partir du fichier CSV
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# 2. Prétraitement des données
# Fusionner les deux ensembles de données sur la colonne 'movieId'
data = pd.merge(ratings, movies, on='movieId')

# 3. Entraînement du modèle
# Diviser les données en un ensemble d'entraînement et un ensemble de test
train_data, test_data = train_test_split(data, test_size=0.2)

# Utiliser la factorisation de matrice pour entraîner le modèle
U, sigma, Vt = svds(train_data, k=50)

# 4. Évaluation du modèle
# Prédire les notes sur l'ensemble de test
test_preds = np.dot(np.dot(U, np.diag(sigma)), Vt)

# Calculer l'erreur quadratique moyenne (RMSE)
rmse = np.sqrt(mean_squared_error(test_data, test_preds))

# 5. Implémentation
# Créer une fonction pour recommander des films à un utilisateur


def recommend_movies(user_id, num_recommendations):
    # Calculer les prédictions pour cet utilisateur
    user_preds = np.dot(np.dot(U[user_id, :], np.diag(sigma)), Vt)

    # Obtenir les indices des films que l'utilisateur n'a pas encore vus
    unseen_movies = np.where(data.iloc[user_id, :] == 0)[0]

    # Obtenir les prédictions pour ces films
    unseen_preds = user_preds[unseen_movies]

    # Obtenir les indices des films recommandés
    recommended_movies = np.argsort(unseen_preds)[-num_recommendations:]

    # Retourner les titres des films recommandés
    return movies.iloc[recommended_movies, :]['title']

# 6. Amélioration continue
# Mettre à jour le modèle avec de nouvelles données et réentraîner le modèle

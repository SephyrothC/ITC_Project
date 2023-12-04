from flask import Flask, render_template
from flask import request

import Movie

# Initialize a Flask application with a template folder
app = Flask(__name__, template_folder='../template')


# Define a route for the home page that accepts both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def home():
    movies_dict = Movie.MovieInit()  # Initialize the movies
    if request.method == 'POST':  # If the request method is POST
        # Get the movie names from the form data and split them by commas
        movie_names = request.form.get('movie_names').split(',')
        # If no movie names were entered
        if not movie_names or movie_names[0] == '':
            # Render the home page with an error message
            return render_template('index.html', error="Please enter at least one movie name.")
        recommended_movies = Movie.recommend_movies(
            movie_names, movies_dict)  # Get the recommended movies
        # Render the home page with the recommended movies
        return render_template('index.html', movies=recommended_movies)
    # If the request method is not POST, render the home page without any movies
    return render_template('index.html')

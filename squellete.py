@app.route('/')
def home():
    movies_dict = MovieInit()
    movie_names = ["Toy Story", "Nemo", "Hercule"]
    recommended_movies = recommend_movies(movie_names, movies_dict)
    return render_template('index.html', movies=recommended_movies)


if __name__ == '__main__':
    average_ratings = {}
    load_average_ratings()
    app.run(debug=True)

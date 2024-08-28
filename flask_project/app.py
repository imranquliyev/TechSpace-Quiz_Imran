from flask import Flask, render_template
from models import db, Movie
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()
with app.app_context():
    if not Movie.query.first():
        sample_movies = [
            Movie(title="Inception", released="2010", director="Christopher Nolan", genre="Sci-Fi"),
            Movie(title="The Matrix", released="1999", director="Wachowski Sisters", genre="Action"),
            Movie(title="Interstellar", released="2014", director="Christopher Nolan", genre="Adventure"),
            Movie(title="The Godfather", released="1972", director="Francis Ford Coppola", genre="Crime"),
            Movie(title="Pulp Fiction", released="1994", director="Quentin Tarantino", genre="Drama"),
            Movie(title="The Dark Knight", released="2008", director="Christopher Nolan", genre="Action")
        ]
        db.session.add_all(sample_movies)
        db.session.commit()
@app.route('/movies/')
def movies():
    all_movies = Movie.query.all()
    return render_template('index.html', movies=all_movies)
@app.route('/movies/<int:movie_id>/')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)
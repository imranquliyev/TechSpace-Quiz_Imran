from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345@localhost:3306/movies_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    released = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

@app.route('/movies/')
def movies():
    all_movies = Movie.query.all()
    return render_template('index.html', movies=all_movies)

@app.route('/movies/<int:movie_id>/')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)

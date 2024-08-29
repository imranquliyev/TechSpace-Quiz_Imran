from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    released = db.Column(db.String(20), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from init import create_app
from flask import Migrate


db = SQLAlchemy()
app = create_app()
# bootstrap database migrate commands
db.init_app(app)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

class Movie(db.Model):
    __tablename__ = 'Movie'

    mid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(50), nullable=False)

    def json(self):
        return {"mID": self.mid, "Title": self.title, "Year" : self.year, "Director": self.director}
    

class Reviewer(db.Model):
    __tablename__ = 'Reviewer'

    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def json(self):
        return {"rID": self.rid, "name": self.name}


class Rating(db.Model):
    __tablename__ = 'Rating'

    rid = db.Column(db.Integer, primary_key=True, nullable=False)
    mid = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    ratingdate = db.Column(db.String(50), nullable=False)

    def json(self):
        return {"rID": self.rid, "mID": self.mid, "stars" : self.stars, "ratingDate": self.ratingdate}
    
    
with app.app_context():
    db.create_all()


@app.route("/test", methods=["GET"]) 
def test():
    return make_response(jsonify({'message': 'test movies'}), 200)


@app.route("/")
def get_movies():
    movies = db.session.execute(db.select(Movie).order_by(Movie.title)).scalars()
    movie_text = '<ul>'
    for movie in movies:
        movie_text += '<li>' + movie.mid + ', ' + movie.title + ', ' + movie.year + ', ' + movie.director + '</li>'
    movie_text += '</ul>'
    return movie_text
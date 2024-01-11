from flask import Flask, render_template, request, jsonify, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import environ

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship, Mapped
from typing import List
from sqlalchemy.orm import joinedload
from collections import defaultdict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'

    mid = db.Column(db.Integer, primary_key=True, self_increment=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(80), nullable=False)
    children_rating: Mapped[List["Rating"]] = relationship(back_populates="parent_movie")
    

    def json(self):
        return {'mid': self.mid, 'title': self.title, 'year': self.year, 'director': self.director }

class Reviewer(db.Model):
    __tablename__ = 'reviewers'

    rid = db.Column(db.Integer, primary_key=True, self_increment=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    children_rating: Mapped[List["Rating"]] = relationship(back_populates="parent_reviewer")
    

    def json(self):
        return {'rid': self.rid, 'name': self.name, 'surname': self.surname, 'age': self.age }
    
class Rating(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True, self_increment=True, nullable=False)
    rid = db.Column(db.Integer, ForeignKey('reviewers.rid'), nullable=False)
    mid = db.Column(db.Integer, ForeignKey('movies.mid'), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    ratingdate = db.Column(db.String(80), nullable=False)

    parent_movie: Mapped["Movie"] = relationship(back_populates="children_rating")
    parent_reviewer: Mapped["Reviewer"] = relationship(back_populates="children_rating")
    

    def json(self):
        return {'rid': self.rid, 'mid': self.mid, 'stars': self.stars, 'ratingdate': self.ratingdate }

with app.app_context():
    db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# create a movie
@app.route('/movies', methods=['POST'])
def create_movies():
  try:
    data = request.get_json()
    new_movie = Movie(title=data['title'], year=data['year'], director=data['director'])
    db.session.add(new_movie)
    db.session.commit()
    return make_response(jsonify({'message': 'movie created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating movie'}), 500)

# create a reviewer
@app.route('/reviewers', methods=['POST'])
def create_reviewers():
  try:
    data = request.get_json()
    new_reviewer = Reviewer(name=data['name'], surname=data['surname'], age=data['age'])
    db.session.add(new_reviewer)
    db.session.commit()
    return make_response(jsonify({'message': 'reviewer created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating reviewer'}), 500)
  
# create a rating
@app.route('/ratings', methods=['POST'])
def create_ratings():
  try:
    data = request.get_json()
    new_rating = Rating(rid=data['rid'], mid=data['mid'], stars=data['stars'], ratingdate=data['ratingdate'])
    db.session.add(new_rating)
    db.session.commit()
    return make_response(jsonify({'message': 'rating created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating rating'}), 500)
  

# get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
  try:
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)
  except e:
    return make_response(jsonify({'message': 'error getting movies'}), 500)
  
# get all reviewers
@app.route('/reviewers', methods=['GET'])
def get_reviewers():
  try:
    reviewers = Reviewer.query.all()
    return render_template('reviewers.html', reviewers=reviewers)
  except e:
    return make_response(jsonify({'message': 'error getting reviewers'}), 500)
  

# get all ratings
@app.route('/ratings', methods=['GET'])
def get_ratings():
    try:
        movie_data = db.session.query(
            Movie,
            func.count(Rating.rid).label('review_count'),
            func.avg(Rating.stars).label('average_rating')
        ).join(Rating).group_by(Movie).all()

        movies = []
        for movie, review_count, average_rating in movie_data:
            reviews = Rating.query.filter_by(parent_movie=movie).all()
            movies.append((movie, review_count, average_rating, reviews))

        return render_template('ratings.html', movies=movies)
    except e:
        return make_response(jsonify({'message': 'error getting ratings'}), 500)
  

# get a movie by id
@app.route('/movies/<int:mid>', methods=['GET'])
def get_movie(mid):
  try:
    movie = Movie.query.filter_by(mid=mid).first()
    if movie:
      return make_response(jsonify({'movie': movie.json()}), 200)
    return make_response(jsonify({'message': 'movie not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting movie'}), 500)
  

# get a reviewer by id
@app.route('/reviewers/<int:rid>', methods=['GET'])
def get_reviewer(rid):
  try:
    reviewer = Reviewer.query.filter_by(rid=rid).first()
    if reviewer:
      return make_response(jsonify({'reviewer': reviewer.json()}), 200)
    return make_response(jsonify({'message': 'reviewer not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting reviewer'}), 500)
  

# get a rating by id
@app.route('/ratings/<int:rating_id>', methods=['GET'])
def get_rating(rating_id):
  try:
    rating = Rating.query.filter_by(rating_id=rating_id).first()
    if rating:
      return make_response(jsonify({'rating': rating.json()}), 200)
    return make_response(jsonify({'message': 'rating not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting rating'}), 500)
  

# update a movie
@app.route('/movies/<int:mid>', methods=['PUT'])
def update_movie(mid):
  try:
    movie = Movie.query.filter_by(mid=mid).first()
    if movie:
      data = request.get_json()
      movie.title = data['title']
      movie.year = data['year']
      movie.director = data['director']
      db.session.commit()
      return make_response(jsonify({'message': 'movie updated'}), 200)
    return make_response(jsonify({'message': 'movie not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating movie'}), 500)


# update a reviewer
@app.route('/reviewers/<int:rid>', methods=['PUT'])
def update_reviewer(rid):
  try:
    reviewer = Reviewer.query.filter_by(rid=rid).first()
    if reviewer:
      data = request.get_json()
      reviewer.name = data['name']
      reviewer.surname = data['surname']
      reviewer.age = data['age']
      db.session.commit()
      return make_response(jsonify({'message': 'reviewer updated'}), 200)
    return make_response(jsonify({'message': 'reviewer not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating reviewer'}), 500)


# update a rating
@app.route('/ratings/<int:rating_id>', methods=['PUT'])
def update_rating(rating_id):
  try:
    rating = Rating.query.filter_by(rating_id=rating_id).first()
    if rating:
      data = request.get_json()
      rating.rid = data['rid']
      rating.mid = data['mid']
      rating.stars = data['stars']
      rating.ratingdate = data['ratingdate']
      db.session.commit()
      return make_response(jsonify({'message': 'rating updated'}), 200)
    return make_response(jsonify({'message': 'rating not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating rating'}), 500)


# delete a movie
@app.route('/movies/<int:mid>', methods=['DELETE'])
def delete_movie(mid):
  try:
    movie = Movie.query.filter_by(mid=mid).first()
    if movie:
      db.session.delete(movie)
      db.session.commit()
      return make_response(jsonify({'message': 'movie deleted'}), 200)
    return make_response(jsonify({'message': 'movie not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting movie'}), 500)


# delete a reviewer
@app.route('/reviewers/<int:rid>', methods=['DELETE'])
def delete_reviewer(rid):
  try:
    reviewer = Reviewer.query.filter_by(rid=rid).first()
    if reviewer:
      db.session.delete(reviewer)
      db.session.commit()
      return make_response(jsonify({'message': 'reviewer deleted'}), 200)
    return make_response(jsonify({'message': 'reviewer not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting reviewer'}), 500)
  

# delete a rating
@app.route('/ratings/<int:rating_id>', methods=['DELETE'])
def delete_rating(rating_id):
  try:
    rating = Rating.query.filter_by(rating_id=rating_id).first()
    if rating:
      db.session.delete(rating)
      db.session.commit()
      return make_response(jsonify({'message': 'rating deleted'}), 200)
    return make_response(jsonify({'message': 'rating not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting rating'}), 500)
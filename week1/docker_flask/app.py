from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email}

with app.app_context():
    # Perform database operations within this block
    db.create_all()

# testing route
@app.route("/test", methods=["GET"]) 
def test():
    return make_response(jsonify({'message': 'test users'}), 200)


# create a user
@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data["username"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify(new_user.json()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# get all users
@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
    

# get a user by id
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify(user.json()), 200)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# update a user by id
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data["username"]
            user.email = data["email"]
            db.session.commit()
            return make_response(jsonify(user.json()), 200)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
    
# delete a user by id
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({"message": "User deleted"}), 200)
        return make_response(jsonify({"error": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


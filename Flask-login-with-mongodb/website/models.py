from . import db
from flask_login import UserMixin

# from sqlalchemy.sql import func

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True),default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')
    
from flask import Flask, jsonify, request, render_template
from passlib.hash import pbkdf2_sha256
import uuid


class User:

    def signup(self):

        # Create the user object
        user = {
        "_id": uuid.uuid4().hex,
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "password1": pbkdf2_sha256.encrypt(request.form.get('password1')),
        "password2": pbkdf2_sha256.encrypt(request.form.get('password2')),
        }
        
        user1 = db.user  # get the user collection in mongobd db
        result = user1.insert_one(user)
        
        return jsonify(user), 200
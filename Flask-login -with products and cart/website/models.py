from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # items = db.relationship('Item', backref='owned_user', lazy=True)
    carts = db.relationship('Cart', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False,unique =True)
    quantity =  db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024),nullable=False,unique =True)
    # user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False)
    quantity =  db.Column(db.Integer(), nullable=False, default=1)
    description = db.Column(db.String(length=1024),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

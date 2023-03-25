from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"

from pymongo import MongoClient

cluster = """mongodb+srv://Akarsh:bJvu6dlkGmrPOQNY@cluster1.ni0a7ss.mongodb.net/mango_mart?retryWrites=true&w=majority"""
client = MongoClient(cluster)

print(client.list_database_names())
db = client.mango_mart
print(db.list_collection_names())

def create_app():
    app = Flask(__name__)
    # app.secret_key = b'\x80\x88\xf7\xb7F\xb1\x83<\xc4\xef9\xed>\xeb\x16\xc0'
    app.config['SECRET_KEY'] = 'brightfutureclub'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    
    # with app.app_context():
    #     db.create_all()
    # create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app

# def create_database(app):
#     if not path.exists('website/'+ DB_NAME):
#         db.create_all(app=app)
#         print('Create Database!')

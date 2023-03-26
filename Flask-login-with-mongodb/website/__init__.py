from flask import Flask
from os import path

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
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
        
    return app


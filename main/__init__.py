from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
import cv2

db = SQLAlchemy()
DB_NAME = "database.db"

def create_database(app):
    if not path.exists("main/"+ DB_NAME):
        db.create_all(app=app)
        print('Created db')


app = Flask(__name__)
app.config["SECRET_KEY"] = "hashedstring"

app.config['UPLOAD_FOLDER'] = '/uploads'


app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from .views import views
from .stream import stream

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(stream, url_prefix="/stream")


# create_database(app)




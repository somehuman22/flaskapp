from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create flask app
app = Flask(__name__)

#configure
app.config.update(
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db',
    SECRET_KEY='password',
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
    DEBUG=True
)

#make database
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import models, views

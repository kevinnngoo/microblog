from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  #represent the database connection
migrate = Migrate(app, db) #represent the migration engine

#import models will define the structure of the database
#importing routes will define the endpoints of the application
from app import routes, models 

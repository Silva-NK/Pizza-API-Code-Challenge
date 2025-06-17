# App setup

from flask import Flask
from flask_migrate import Migrate

from .models.db import db
from .config import Config
from .models import Restaurant, Pizza, RestaurantPizza

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)   
    
    db.init_app(app)
    Migrate(app, db)

    return app

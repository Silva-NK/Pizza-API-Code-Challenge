# App setup

from flask import Flask
from flask_migrate import Migrate

from .config import Config

from .models.db import db
from .models import Restaurant, Pizza, RestaurantPizza

from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_controller import restaurant_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp


app = Flask(__name__)
app.config.from_object(Config)   
    
db.init_app(app)
Migrate(app, db)

@app.route('/')
def home():
    return {"message": "Welcome to Pizza API!!!"}
    
# Blueprint driven routes
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
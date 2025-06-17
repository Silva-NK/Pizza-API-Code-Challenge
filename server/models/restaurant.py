# Models (SQLAlchemy)

from flask_sqlalchemy import SQLAlchemy

from .db import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates = "restaurant", cascade = 'all, delete')
    pizzas = db.relationship('Pizza', secondary = "restaurant_pizzas", back_populates = "restaurant")

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.address}>"
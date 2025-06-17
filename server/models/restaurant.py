# Models (SQLAlchemy)

from flask_sqlalchemy import SQLAlchemy

from .db import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates = "restaurant", cascade = 'all, delete')

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.address}>"
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [pizza.to_dict() for pizza in self.pizzas]
        }
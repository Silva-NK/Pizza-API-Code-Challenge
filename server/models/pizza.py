# Models (SQLAlchemy)# Models (SQLAlchemy)

from flask_sqlalchemy import SQLAlchemy

from .db import db

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    ingredients = db.Column(db.String, nullable = False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates = "pizza", cascade = 'all, delete-orphan')
    restaurants = db.relationship('Restaurant', secondary = "restaurant_pizzas", back_populates = "pizza")

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name}, {self.ingredients}>"
# Models (SQLAlchemy)# Models (SQLAlchemy)

from flask_sqlalchemy import SQLAlchemy

from .db import db

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer, nullable = False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id', ondelete = 'CASCADE'), nullable = False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id', ondelete = 'CASCADE'), nullable = False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def __repr__(self):
        return f"<Restaurant_Pizza {self.id}: {self.pizza.name} for ${self.price} at {self.restaurant.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id,
            "pizza": self.pizzas.to_dict() if self.pizzas else None,
            "restaurant": self.restaurants.to_dict() if self.restaurants else None
        }
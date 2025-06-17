# Route Handlers

from flask import Blueprint, jsonify, request

from ..models.db import db
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix = '/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods = ['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    pizza = db.session.get(Pizza, pizza_id)
    restaurant = db.session.get(Restaurant, restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 404
    
    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify(rp.to_dict()), 201
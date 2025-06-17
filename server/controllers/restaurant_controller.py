# Route Handlers

from flask import Blueprint, jsonify

from ..models.db import db
from ..models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__, url_prefix = '/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    restaurant_dict = [r.to_dict() for r in restaurants]
    return jsonify(restaurant_dict), 200

@restaurant_bp.route("/<int:id>", methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = db.session.get(Restaurant, id)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    return jsonify(restaurant.to_dict()), 200

@restaurant_bp.route("/<int:id>", methods=['DELETE'])
def delete_restaurant(id):
    restaurant = db.session.get(Restaurant, id)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204
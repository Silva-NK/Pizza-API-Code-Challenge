# Route Handlers

from flask import Blueprint, jsonify

from ..models.db import db
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__, url_prefix = '/pizzas')

@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()

    pizzas_dict = [p.to_dict() for p in pizzas]
    return jsonify(pizzas_dict), 200
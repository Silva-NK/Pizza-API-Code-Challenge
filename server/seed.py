# Seed data

from server.app import app
from server.models.db import db

from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

def clear_tables():
    print ("Clearing old database data...")

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    db.session.commit()

    print ("Clearing database complete...")

def seed_tables():
    print ("Seeding database...")

    rest1 = Restaurant(name="Domino Tower Pizza", address="123 Slice Street, Mozzarella City")
    rest2 = Restaurant(name="Papa Mozza", address="45 Cheesy Crust Ave, Doughville")
    rest3 = Restaurant(name="The Saucy Wheel", address="789 Oven Lane, Tomato Town")
    rest4 = Restaurant(name="Pie Republic", address="321 Topping Blvd, Pizza Plains")
    rest5 = Restaurant(name="Kiki's Fire Pizza", address="654 Brick Oven Rd, Pepperoni Park")

    db.session.add_all([rest1, rest2, rest3, rest4, rest5])
    db.session.commit()



    pie1 = Pizza(name="Tropic Thunder", ingredients="Dough, Tomato Sauce, Mozzarella, Ham, Pineapple")
    pie2 = Pizza(name="Meat Inferno", ingredients="Dough, BBQ Sauce, Pepperoni, Sausage, Bacon, Ham")
    pie3 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Olives, Bell Peppers, Onions, Mushrooms")
    pie4 = Pizza(name="Four Cheese Blaze", ingredients="Dough, Tomato Sauce, Mozzarella, Parmesan, Gouda, Gorgonzola")
    pie5 = Pizza(name="Garlic Chicken Feast", ingredients="Dough, Garlic Cream Sauce, Grilled Chicken, Spinach, Red Onions")
    pie6 = Pizza(name="Spicy Pepperoni Rush", ingredients="Dough, Tomato Sauce, Mozzarella, Double Pepperoni, Jalapeños")
    pie7 = Pizza(name="Mushroom Majesty", ingredients="Dough, Cream Sauce, Mozzarella, Mushrooms, Thyme, Truffle Oil")
    pie8 = Pizza(name="BBQ Ranch Rodeo", ingredients="Dough, BBQ Sauce, Chicken, Red Onion, Ranch Drizzle")
    pie9 = Pizza(name="Sun-Dried Garden", ingredients="Dough, Tomato Sauce, Sun-Dried Tomatoes, Artichokes, Feta, Arugula")
    pie10 = Pizza(name="Zesty Pesto Pie", ingredients="Dough, Pesto Sauce, Cherry Tomatoes, Mozzarella, Basil")

    db.session.add_all([ pie1, pie2, pie3, pie4, pie5, pie6, pie7, pie8, pie9, pie10])
    db.session.commit()



    rp1 = RestaurantPizza(price=15, restaurant=rest1, pizza=pie1)
    rp2 = RestaurantPizza(price=20, restaurant=rest1, pizza=pie2)
    rp3 = RestaurantPizza(price=12, restaurant=rest1, pizza=pie3)
    rp4 = RestaurantPizza(price=18, restaurant=rest2, pizza=pie4)
    rp5 = RestaurantPizza(price=14, restaurant=rest2, pizza=pie5)
    rp6 = RestaurantPizza(price=16, restaurant=rest3, pizza=pie6)
    rp7 = RestaurantPizza(price=22, restaurant=rest3, pizza=pie1)
    rp8 = RestaurantPizza(price=13, restaurant=rest4, pizza=pie7)
    rp9 = RestaurantPizza(price=19, restaurant=rest4, pizza=pie8)
    rp10 = RestaurantPizza(price=17, restaurant=rest5, pizza=pie9)
    rp11 = RestaurantPizza(price=21, restaurant=rest5, pizza=pie10)
    rp12 = RestaurantPizza(price=12, restaurant=rest5, pizza=pie3)
    rp13 = RestaurantPizza(price=23, restaurant=rest2, pizza=pie10)
    rp14 = RestaurantPizza(price=11, restaurant=rest3, pizza=pie4)
    rp15 = RestaurantPizza(price=14, restaurant=rest4, pizza=pie2)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6, rp7, rp8, rp9, rp10, rp11, rp12, rp13, rp14, rp15])
    db.session.commit()

    print("Seeding complete...")

if __name__ == "__main__":
    with app.app_context():
        clear_tables()
        seed_tables()

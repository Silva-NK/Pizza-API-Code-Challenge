# PIZZA API CODE CHALLENGE
## Introduction

Pizza API is a lightweight RESTful-like backend application for managing restaurants, pizzas, and their associations. It provides basic CRUD functionality and data validation, allowing users to list restaurants and pizzas, retrieve specific details, delete restaurants, and associate pizzas with restaurants. The app is built using Flask, SQLAlchemy, and Alembic for migrations.

## MVC Structure
.
├── challenge-1-pizzas.postman_collection.json
├── instance
│   └── app.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── __pycache__
│   │   └── env.cpython-312.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── e4a02e012628_initial_migration.py
│       └── __pycache__
│           └── e4a02e012628_initial_migration.cpython-312.pyc
├── Pipfile
├── Pipfile.lock
├── README.md
└── server
    ├── app.py
    ├── config.py
    ├── controllers
    │   ├── __init__.py
    │   ├── pizza_controller.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── pizza_controller.cpython-312.pyc
    │   │   ├── restaurant_controller.cpython-312.pyc
    │   │   └── restaurant_pizza_controller.cpython-312.pyc
    │   ├── restaurant_controller.py
    │   └── restaurant_pizza_controller.py
    ├── __init__.py
    ├── models
    │   ├── db.py
    │   ├── __init__.py
    │   ├── pizza.py
    │   ├── __pycache__
    │   │   ├── db.cpython-312.pyc
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── pizza.cpython-312.pyc
    │   │   ├── restaurant.cpython-312.pyc
    │   │   └── restaurant_pizza.cpython-312.pyc
    │   ├── restaurant_pizza.py
    │   └── restaurant.py
    ├── __pycache__
    │   ├── app.cpython-312.pyc
    │   ├── config.cpython-312.pyc
    │   ├── __init__.cpython-312.pyc
    │   └── seed.cpython-312.pyc
    └── seed.py

12 directories, 38 files


## Setup Instructions

1. **Install dependencies and create a virtual environment:**

    > 1. Clone the repository
    > 2. Run `pipenv install` to install dependencies.
    > 3. Run `pipenv shell` to activate virtual environment.
    > 4. Run `export FLASK_APP=server/app.py` followed by `export FLASK_RUN_PORT=5555` to set up environment variables.
    > 5. Finally to run use `flask run`.

### Optional instructions

If creating different database Models and seeking to save them use:
    > `flask db init`(Use only once)
    > `flask db migrate -m "Initial migration"` (Change the qouted text to meet migration conditions.)
    > `flask db upgrade`

If you wish to make use of the seed data in seed.py:
    > Run `python -m server.seed`

If you wish to use the Flask shell, use:
    > Run `flask shell`

## Route Summary
1. Landing Page : `/` : OPens Landing page
2. GET :  `/restaurants` :	List all restaurants
3. GET :  `/restaurants/<id>` :	Retrieve one restaurant & its pizzas
4. DELETE : `/restaurants/<id>` : Delete a restaurant and its relationships
5. GET : `/pizzas` : List all pizzas
6. POST: `/restaurant_pizzas` : Create restaurant-pizza relationship

### Example requests & responses for each route

1. Landing Page - `http://127.0.0.1:5555`:

    `{"message":"Welcome to Pizza API!!!"}`

2. GET /restaurants - `http://127.0.0.1:5555/restaurants`:

    [
        {
            "address": "123 Slice Street, Mozzarella City",
            "id": 1,
            "name": "Domino Tower Pizza"
        },
        {
            "address": "789 Oven Lane, Tomato Town",
            "id": 3,
            "name": "The Saucy Wheel"
        },
        ...
    ]

3. GET /restaurants/<int:id> - `http://127.0.0.1:5555/restaurants/3`:
    > If found:

        {
            "address": "789 Oven Lane, Tomato Town",
            "id": 3,
            "name": "The Saucy Wheel"
        }

    > If not found:

        {
            "error": "Restaurant not found"
        }

4. DELETE /restaurants/<int:id> - `http://127.0.0.1:5555/restaurants/3`:
    > If found:

        (no content, status 204)

    > If not found:

        {
            "error": "Restaurant not found"
        }

5. GET /pizzas - `http://127.0.0.1:5555/pizzas`:

    [
        {
            "id": 1,
            "ingredients": "Dough, Tomato Sauce, Mozzarella, Ham, Pineapple",
            "name": "Tropic Thunder"
        },
        {
            "id": 2,
            "ingredients": "Dough, BBQ Sauce, Pepperoni, Sausage, Bacon, Ham",
            "name": "Meat Inferno"
        },
        ...
    ]

6. POST /restaurant_pizzas - `http://127.0.0.1:5555/restaurant_pizzas`:

    Add request:

    {
        "price": 5,
        "pizza_id": 1,
        "restaurant_id": 3
    }

    Successful response:

    {
        "id": 4,
        "price": 5,
        "pizza_id": 1,
        "restaurant_id": 3,
        "pizza": {
            "id": 1,
            "name": "Emma",
            "ingredients": "Dough, Tomato Sauce, Cheese"
        },
        "restaurant": {
            "id": 3,
            "name": "Kiki's Pizza",
            "address": "address3"
        }
    }

    Validation Error (price out of range)::

    {
        "errors": ["Price must be between 1 and 30"]
    }

    Foreign Key Error (IDs don't exist): 

    {
        "errors": ["Invalid pizza_id or restaurant_id"]
    }

## Validation rules
- `price` must be between 1 and 30 in POST /restaurant_pizzas.
- `pizza_id` and `restaurant_id` must exist in the database or 404 will be returned.
- Deleting a restaurant also deletes related restaurant-pizzas.


## Using Postman
The file `challenge-1-pizzas.postman_collection.json` already contain the collection for testing in postman.
Therefore to use Postman:

1. Open Postman
2. Click "Import"
3. Select the file`challenge-1-pizzas.postman_collection.json` or drag and drop it into the selsction box.
4. Ensure the base URL matches you Flask server either `http://localhost:5555/` or `http://127.0.0.1:5555/`
5. Test each route by clicking "Send".


**NOTE:** When using Postman best to have you server running, which, as earlier mentioned uses `flask run` in the project root folder in the terminal.


## Resources

- [Tullier-Blog-CLI-Project Git Repo](https://github.com/Silva-NK/Pizza-API-Code-Challenge)

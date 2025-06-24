from db import users, products, orders
from datetime import datetime

def register_user(username, password, role='user'):
    if users.find_one({"username": username}):
        return False
    users.insert_one({"username": username, "password": password, "role": role})
    return True

def login_user(username, password):
    return users.find_one({"username": username, "password": password})

def add_product(name, price, stock):
    products.insert_one({"name": name, "price": price, "stock": stock})

def list_products():
    return list(products.find())

def search_product(name):
    return list(products.find({"name": {"$regex": name, "$options": "i"}}))

def place_order(username, product_id, quantity):
    product = products.find_one({"_id": product_id})
    if not product:
        return "Product not found."
    if product['stock'] < quantity:
        return "Out of Stock or insufficient quantity."

    products.update_one({"_id": product_id}, {"$inc": {"stock": -quantity}})
    orders.insert_one({
        "username": username,
        "product_id": product_id,
        "product_name": product['name'],
        "quantity": quantity,
        "total_price": quantity * product['price'],
        "date": datetime.now()
    })
    return "Order placed successfully."


def user_orders(username):
    return list(orders.find({"username": username}))

def get_all_orders():
    return list(orders.find())

def get_all_users():
    return list(users.find())
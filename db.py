from pymongo import MongoClient

# Update this URI as needed
client = MongoClient("mongodb://localhost:27017/")
db = client['shopcli_db']

users = db['users']
products = db['products']
orders = db['orders']
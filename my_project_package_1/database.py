from config import get_db

db = get_db()
collection = db["products_python2025_dato"]

def setup_data():
    collection.delete_many({})
    items = [
        {"name": "Pen", "price": 1.5, "stock": 10},
        {"name": "Notebook", "price": 3.99, "stock": 5},
        {"name": "Backpack", "price": 25.0, "stock": 2}
    ]


    collection.insert_many(items)
    print(f"{len(items)} products inserted.")

def update_prices():
    for p in collection.find():
        new_price = round(p['price'] * 1.2, 2)
        collection.update_one({"_id": p['_id']}, {"$set": {"price": new_price}})

def get_all_products():
    return collection.find()
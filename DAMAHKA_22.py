##   Выбор заказов

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
###########################################################

def get_premium_products(order_list):
    expensive_orders = filter(lambda x: x["price"] > 500, order_list)
    product_names = map(lambda x: x["product"], expensive_orders)
    final_list = sorted(product_names)
    return final_list
result = get_premium_products(orders)
print(result)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#         Статистика продаж
sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]

from collections import defaultdict

revenue_dict = defaultdict(int)
for item,cal,price in sales:
    revenue_dict[item] += cal * price
sorted_result = dict(sorted(revenue_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_result)


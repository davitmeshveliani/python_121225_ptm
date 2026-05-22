from database import setup_data, update_prices, get_all_products

if __name__ == "__main__":

    setup_data()
    update_prices()

    print("Prices updated for 3 products.\n")
    print("Updated products:")
    for p in get_all_products():
        print(f"- {p['name']} - ${p['price']:.2f}")
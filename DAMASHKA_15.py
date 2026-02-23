
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']
#################### 1 ##############################################
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# result = []
# for item in text_list:
#     if len(item.split()) == 1:
#         result.append(item.lower())
# print("Обработанный список:", result)

############# 2 ###############################
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#
# discount = float(input("Введите скидку (%): "))
#
# print(f"{'Товар':<15}{'Старая цена':<15}{'Новая цена'}")
# print("-" * 40)
# for product in products:
#     name = product[0]
#     alt_preis = product[1]
#     neu_preis = alt_preis * (1 - discount / 100)
#     product.append(neu_preis)
#     print(f"{name:<15}{alt_preis:>10.2f}$   {neu_preis:>10.2f}$")

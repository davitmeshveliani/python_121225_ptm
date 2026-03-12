# def is_prime(n):
#     if n < 2:
#        return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Введите число:"))
# if is_prime(n):
#     print(f"Число {n} является простым")
# else:
#     print(f"Число {n} не является простым")


############  2 Фильтрация чисел по чётности #############

# def filter_numbers(filter_type, *numbers):
#     if filter_type == "even":
#         return [n for n in numbers if n % 2 == 0]
#     elif filter_type == "odd":
#         return [n for n in numbers if n % 2 != 0]
#     else:
#         return "Некорректный фильтр"
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))

########## 3 Объединение словарей #################

# def nun_dicts(*dicts):
#     res = {}
#     for d in dicts:
#         res.update(d)
#     return res
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}
# nun_1 = nun_dicts(dict1, dict2, dict3)
# print(nun_1)
#############################
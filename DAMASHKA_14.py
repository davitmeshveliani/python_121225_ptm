 ###############################################

# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# result = []
# for s in strings:
#     for index, ch in enumerate(s):
#         if ch.isdigit():
#             break
#     else:
#         continue
#     letters = s[:index]
#     digits = s[index:]uuuuuuuuun
#     if letters.isalpha() and digits.isdigit():
#         result.append(s)
# print("Строки с цифрами только в конце:",result)
#######################################################

#################

# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# num = int(input("Введите число для удаления кратных ему элементов: "))
# nun_neu = []
# for x in numbers:
#     if x % num != 0:
#         nun_neu.append(x)
# print("Список без кратных значений:", nun_neu)
##########################################################

# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
#
# nun_neu = sorted([x for x in numbers if x % 2 == 0], reverse=True)
#
# result = []
# i = 0
# for x in numbers:
#     if x % 2 == 0:
#         result.append(nun_neu[i])
#         i += 1
#     else:
#         result.append(x)
#
# print("Список после сортировки:",result)

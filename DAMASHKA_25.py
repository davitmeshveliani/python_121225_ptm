# def divide_numbers(x, y):
#     try:
#         x = float(x)
#         y = float(y)
#     except ValueError:
#         raise ValueError("Ошибка: Введено некорректное число.")
#
#     if y == 0:
#         raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")
#
#     return x / y
# result = divide_numbers(0, "k")

# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ß
# import logging
#
# logging.basicConfig(
#     level=logging.ERROR,
#     format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
# )
#
# def divide_numbers(x, y):
#     try:
#         x = float(x)
#         y = float(y)
#
#         if x == 0:
#             raise ZeroDivisionError("Ошибка: ни одно значение не должно быть нулем.")
#
#         if y == 0:
#             raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")
#
#         return x / y
#
#     except ValueError:
#         logging.error("Ошибка: Введено некорректное число.")
#         return
#
#     except ZeroDivisionError as e:
#         logging.error(str(e))
#         return
#
#     except Exception:
#         logging.error("Системная ошибка.")
#         return
#
#
# divide_numbers(0, "k")
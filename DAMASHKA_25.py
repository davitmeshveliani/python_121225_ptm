
def divide_numbers():
    """
     This function asks the user for two numbers
     and performs division.

     Handles errors:
     - ValueError: if the input is not a valid number
     - ZeroDivisionError: if the divisor is zero
     - Exception: any other unexpected errors
    """

    try:
          x = float(input("Введите делимое: "))
          y = float(input("Введите делитель: "))
          result = x / y
    except ValueError:
         print("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
    except Exception as er:
        print("Непредвиденная ошибка:", er)
    else:
        print("Результат:", result)

divide_numbers()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ß

import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    encoding="utf-8",
    format="%(asctime)s - ERROR - %(filename)s: Line %(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
def divide_number():
    """
        Prompts the user for two numbers and performs division.

        Validates input types, ensures the dividend is not zero (custom rule),
        and handles potential exceptions like ZeroDivisionError.
        Logs errors to 'errors.log' with specific details.
        """

    try:
        a_input = input("Введите делимое: ")
        b_input = input("Введите делитель: ")

        a = float(a_input)
        b = float(b_input)

        if a == 0:
            raise ValueError("Ошибка: Делимое не должно быть нулем.")
        result = a / b


    except ValueError as er:

        log_msg = f"Ошибка: Некорректный ввод." #: {er}" if "could not convert" in str(er) else str(er)
        logging.error(log_msg)                    # Я сделал это для того, чтобы лог было легче читать и чтобы
                                                   # он точно показывал, где и какая проблема возникает.
                                                   #Как вы думаете, это хороший подход? Что бы вы посоветовали?

        print("Ошибка: Введено некорректное число. ")#
                                                  #

    except ZeroDivisionError as er:
        msg = "Ошибка: Деление на ноль невозможно."
        logging.error(msg)
        print(msg)

    except Exception as er:
        msg = f"Непредвиденная ошибка: {er}"
        logging.error(msg)
        print(msg)
    else:
        print("Результат:", result)
divide_number()

def divide_numbers():
    try:
        x = float(input("Введите делимое: "))
        if x == 0:
            raise ZeroDivisionError("Ошибка: ни одно значение не должно быть нулем.")

        y = float(input("Введите делитель: "))
        if y == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")

        return x / y

    except ValueError:
        raise ValueError("Ошибка: Введено некорректное число.")

    except ZeroDivisionError:
        raise
    except Exception:
        raise Exception("Системная ошибка.")
divide_numbers()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ß
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
)


def divide_numbers():
    try:
        x = float(input("Введите делимое: "))
        if x == 0:
            raise ZeroDivisionError("Ошибка: ни одно значение не должно быть нулем.")

        y = float(input("Введите делитель: "))
        if y == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")

        return x / y

    except ValueError:
        msg = "Ошибка: Введено некорректное число."
        logging.error(msg)
        return

    except ZeroDivisionError as e:
        msg = str(e)
        logging.error(msg)
        return

    except Exception:
        msg = "Системная ошибка."
        logging.error(msg)
        return
divide_numbers()
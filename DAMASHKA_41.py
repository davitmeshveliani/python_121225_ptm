
import pymysql
from pymysql.cursors import DictCursor

config = {
    'host': 'ich-db.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'password',
    'database': 'world',
    'cursorclass': DictCursor
}

connection = None

try:
    connection = pymysql.connect(**config)

    with connection.cursor() as cursor:

        cursor.execute("SELECT Name FROM country;")
        countries = cursor.fetchall()

        # print("1. Список всех стран:")  # Это для меня
        for index, country in enumerate(countries, start=1):
            print(f"{index}. {country['Name']}")

        print("\n" + "=" * 40 + "\n")

        selected_country = input("Введите страну: ").strip()
        num = """
            SELECT city.Name AS CityName, city.Population 
            FROM city 
            JOIN country ON city.CountryCode = country.Code 
            WHERE country.Name = %s
            ORDER BY city.Population DESC;
        """

        cursor.execute(num, (selected_country,))
        cities = cursor.fetchall()

        if not cities:
            raise ValueError(f"Страна '{selected_country}' не найдена или в ней нет городов.")
        print(f"\nГорода выбранной страны ({selected_country}):")

        for index, city in enumerate(cities, start=1):
            print(f"{index}. {city['CityName']} – {city['Population']}")

        connection.commit()
        # print("\n[Транзакция успешно завершена - Commit]")   # Это для меня

except Exception as e:
    print(f"\nПроизошла ошибка: {e}")
    if connection is not None:
        connection.rollback()
        # print("[Транзакция отменена - Rollback]")  # Это для меня

finally:
    if connection is not None:
        connection.close()
        # print("[Соединение с БД закрыто]") # Это для меня
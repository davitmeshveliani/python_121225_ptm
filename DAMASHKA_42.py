import pymysql
from pymysql.cursors import DictCursor

config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'cursorclass': DictCursor,
}

db_name = "notes_app_121225-ptm_davit"

connection = None

try:
    connection = pymysql.connect(**config)

    with connection.cursor() as cursor:

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
        cursor.execute(f"USE `{db_name}`")
        print(f"Database '{db_name}' created or already exists.")

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT
            )
        """)

        cursor.execute("DELETE FROM notes")

        insert_query = "INSERT INTO notes (title, content) VALUES (%s, %s)"
        cursor.execute(insert_query, ("Shopping list", "Milk, Bread, Eggs"))

        connection.commit()
        # print("\n[Транзакция успешно завершена - Commit]")  # Это для меня

        cursor.execute("SELECT * FROM notes")
        all_notes = cursor.fetchall()

        # print("\nВсе заметки в базе данных:")  # Это для меня
        for note in all_notes:
            print(f"Note added: {note['title']}")

except Exception as e:
    print(f"\n[Ошибка при работе с БД]: {e}")
    if connection is not None:
        connection.rollback()
        # print("[Транзакция отменена - Rollback]")  # Это для меня

finally:
    if connection is not None:
        connection.close()
        # print("\n[Соединение с базой данных успешно закрыто]")  # Это для меня
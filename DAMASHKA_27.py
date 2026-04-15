# filename = input("Введите имя файла для поиска: ")
# key_word = input("Введите ключевое слово: ").strip()
#
# try:
#     with open(filename, "r", encoding="utf-8") as f_neu:
#         results = [line for line in  f_neu if key_word.lower() in line.lower()]
#     if results:
#         new_filename = f"{key_word}_{filename}"
#         with open(new_filename, "w", encoding="utf-8") as out:
#             out.writelines(results)
#         print(f"Строки, содержащие '{key_word}', сохранены в {new_filename}")
#     else:
#         print(f"Совпадений со словом '{key_word}' не найдено. Файл не создан.")
# except FileNotFoundError:
#     raise FileNotFoundError(f"Ошибка: Файл {filename} не найден.")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
filename = input("Введите имя файла: ").strip()
try:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    unique_lines = []
    for movie in lines:
        if movie not in unique_lines:
            unique_lines.append(movie)
    new_filename = f"unique_{filename}"
    with open(new_filename, "w", encoding="utf-8") as out:
        out.write("\n".join(unique_lines))
    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")
except FileNotFoundError:
    raise FileNotFoundError(f"Ошибка: Файл {filename} не найден.")

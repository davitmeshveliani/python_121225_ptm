import os
import sys

if len(sys.argv) < 2:
    print("Ошибка: Укажите путь к директории в аргументах.")
    sys.exit()

path = sys.argv[1]

if not os.path.exists(path):
    print(f"Путь '{path}' не существует.")
    sys.exit()

if not os.path.isdir(path):
    print(f"'{path}' не является директорией.")
    sys.exit()

try:
    items = os.listdir(path)
except Exception as e:
    print(f"Ошибка доступа: {e}")
    sys.exit()

folders = []
files = []

for item in items:
    full_path = os.path.join(path, item)
    if os.path.isdir(full_path):
        folders.append(item)
    else:
        files.append(item)

folders.sort()
files.sort()

print(f"Содержимое директории '{path}':\n")

print(f"Папки ({len(folders)}):")
for f in folders:
    print(f"- {f}")

print(f"\nФайлы ({len(files)}):")
for f in files:
    print(f"- {f}")
#
# # /////////////////////////////////////////

import os
import sys

if len(sys.argv) < 3:
    print("Ошибка: Укажите путь к директории и расширение файла (например: .log)")
    sys.exit()

target_path = sys.argv[1]
extension = sys.argv[2]

if not os.path.exists(target_path):
    print("Ошибка: Указанный путь не существует.")
    sys.exit()

if not os.path.isdir(target_path):
    print("Ошибка: Это не директория.")
    sys.exit()

found_files = []

for root, dirs, files in os.walk(target_path):
    for file in files:
        if file.lower().endswith(extension.lower()):
            found_files.append(os.path.join(root, file))

if not found_files:
    print(f"Файлы с расширением '{extension}' не найдены.")
    sys.exit()

print(f"Найдены файлы с расширением '{extension}':")
for f in found_files:
    print(f"- {os.path.relpath(f, target_path)}")

confirm = input("\nВы хотите удалить эти файлы? (y/n): ").lower()

if confirm == 'y':
    for f in found_files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Ошибка при удалении {f}: {e}")
    print("Удаление завершено.")
else:
    print("Удаление отменено.")
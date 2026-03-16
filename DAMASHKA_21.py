# Реализуйте функцию, которая принимает текст
# и возвращает словарь
# с подсчётом количества каждой буквы,
# игнорируя регистр.
# Данные:
# text = "Programming is fun!"
# Пример вывода:
#
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1
# /////////////////////////////////////

from collections import Counter
text = "Programming is fun!"
result = Counter(c for c in text.lower() if c.isalpha())
print(dict(result))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

# ///////////////////////////////////////////////////
from collections import defaultdict
students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy")
]
groups = defaultdict(list)
for class_name, student in students:
    groups[class_name].append(student)
print(dict(groups))



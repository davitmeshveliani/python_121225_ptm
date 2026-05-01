
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return  self.width * self.height

rec = Rectangle(5, 4)
print("Площадь:", rec.get_area())

rec.width = 5
rec.height = 7
print("Новая площадь:", rec.get_area())

############################################################
class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
        return f"Значение увеличено: {self.value}"
    def decrement(self):
        self.value -= 1
        return f"Значение уменьшено: {self.value}"
    def get_value(self):
        return self.value
counter = Counter()

print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.decrement())
print(f"Текущее значение: {counter.get_value()}")

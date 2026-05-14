from abc import ABC, abstractmethod
import math

class InvalidSizeError(Exception):
    """Ошибка неверного размера фигуры."""
    pass

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь фигуры."""
        pass

class Circle(Shape):

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidSizeError(
                "Радиус должен быть положительным числом.")

        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    def area(self) -> float:
        return math.pi * self.__radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.__radius})"

class Rectangle(Shape):

    def __init__(self, width: float, height: float):

        if width <= 0 or height <= 0:
            raise InvalidSizeError(
                "Ширина и высота должны быть положительными числами."
            )

        self.__width = width
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height

    def area(self) -> float:
        return self.__width * self.__height

    def __str__(self) -> str:
        return (
            f"Rectangle(width={self.__width}, "
            f"height={self.__height})"
        )

try:
    shapes: list[Shape] = [
        Circle(3),
        Rectangle(3, 5)
    ]
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area():.2f}")
        print("-" * 30)

except InvalidSizeError as error:
    print(f"Ошибка: {error}")
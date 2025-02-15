import math

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class CircleInSquare(Square, Circle):
    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)

    def __str__(self):
        return (
            f"Квадрат, сторона = {self.side_length}, "
            f"площадь = {self.area()}, "
            f"периметр = {self.perimeter()}\n"
            f"Окружность, радиус = {self.radius}, "
            f"площадь = {self.area()}, "
            f"длина окружности = {self.circumference():.2f}"
        )

shape = CircleInSquare(10)
print(shape)
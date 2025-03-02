class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = self.height = width  # Нарушает LSP

    def set_height(self, height):
        self.width = self.height = height  # Нарушает LSP


# --- Тестируем код ---
def test_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f"Expected area: 50, Got: {rectangle.get_area()}")  # Ожидаем 50


rect = Rectangle(2, 3)
test_area(rect)  # Работает правильно

sq = Square(4)
test_area(sq)  # Ошибка! Ожидаем 50, но получаем 100

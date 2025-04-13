"""
flyweight

фигуры - много на холсте - внутреннее состояние
круги
квадраты
треугольники

тип фигуры - фигуры
цвет
координаты на холсте x y - внешнее состояние

ShapeType - тип фигуры и цвет
ShapeFactory - создает и кеширует ShapeType
Shape - одна фигура: координаты и ссылка на ShapeType
Canvas - контейнер, все Shape. draw_all()
"""

class ShapeType:
    def __init__(self, shape_name: str, color: str):
        self.shape_name = shape_name
        self.color = color

    def draw(self, x, y):
        print(f"рисуем {self.shape_name.upper()} ({self.color}) на ({x} {y})")

class ShapeFactory:
    _types = {}

    @classmethod
    def get_shape_type(cls, shape_name, color):
        key = (shape_name, color)
        if key not in cls._types:
            cls._types[key] = ShapeType(shape_name, color)
            print(f"[Factory] новый тип {shape_name} {color}")
        return cls._types[key]

class Shape:
    def __init__(self, x, y, shape_type: ShapeType):
        self.x = x
        self.y = y
        self.shape_type = shape_type

    def draw(self):
        self.shape_type.draw(self.x, self.y)

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, x, y, shape_name, color):
        shape_type = ShapeFactory.get_shape_type(shape_name, color)
        shape = Shape(x, y, shape_type)
        self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            shape.draw()

canvas = Canvas()

canvas.add_shape(10, 20, "circle", 'red')

canvas.draw_all()
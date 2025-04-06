"""
protocol
протокол Drawable
классы Circle, Square, Image - для каждого draw()
без наследования
"""

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def draw(self) -> None:
        print(f"рисуем с радиус {self.radius}")

class Square:
    def __init__(self, side: int):
        self.side = side

    def draw(self) -> None:
        print(f"квадрат с сторона {self.side}")

class TextBlock:
    def __init__(self, text: str):
        self.text = text

    def draw(self) -> None:
        print(f"текст {self.text}")

def render_scene(drawables: list[Drawable]) -> None:
    print('начало')
    for drawable in drawables:
        drawable.draw()
    print('конец')


circle1 = Circle(10)
square1 = Square(5)
text1 = TextBlock("hi")

scene_objects = [circle1, square1, text1]

render_scene(scene_objects)
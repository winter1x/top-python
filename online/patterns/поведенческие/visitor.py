"""
позволяет добавлять новое поведение
"""
"""
выносит обработку объектов в отдельный класс - посетитель
новое добавить отдельным классом
объекты принимают посетителя и передают ему управление
accept(visitor)
visitor.visit(self)


(+)
добавляем новые операции, не меняя классы объектов
упрощает поддержку и расширение кода
соблюдает OCP - открыт для расширения, закрыт для модификации

(-)
может усложняет код, если объектов много
новые типы объекта требуют добавления метода в Visitor
"""
#плохой код
"""class Text:
    def __init__(self, context):
        self.context = context

    def render(self):
        return self.context

class Image:
    def __init__(self, file_name):
        self.file_name = file_name

    def render(self):
        return f"фото {self.file_name}"

elements = [Text('привет мир'), Image('cat.jpg')]"""

#хороший

from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Text(Element):
    def __init__(self, context):
        self.context = context

    def accept(self, visitor):
        return visitor.visit_text(self)


class Image(Element):
    def __init__(self, file_name):
        self.file_name = file_name

    def accept(self, visitor):
        return visitor.visit_image(self)

class Visitor(ABC):
    @abstractmethod
    def visit_text(self, text):
        pass

    def visit_image(self, image):
        pass

class HTMLRenderer(Visitor):
    def visit_text(self, text):
        print(f"<p>{text.context}</p>")

    def visit_image(self, image):
        print(f"<img src='{image.file_name}' />")

elements = [Text('привет мир'), Image('cat.jpg')]

html_renderer = HTMLRenderer()
for elem in elements:
    elem.accept(html_renderer)

"""
реализуйтеп JSONExporter

пример вывода
{"type": "text", "content": "привет мир"}
{"type": "image", "content": "cat.jpg"}
"""
import json

class JSONExporter(Visitor):
    def visit_text(self, text):
        return json.dumps({"type": "text", "context": text.context}, ensure_ascii=False)

    def visit_image(self, image):
        return json.dumps({"type": "image", "context": image.file_name}, ensure_ascii=False)

json_exporter = JSONExporter()
for elem in elements:
    print(elem.accept(json_exporter))


"""
система обработки различных геометрических фигур (круг, прямоугольник, треугольник)
разные операции (вычисление площади, периметра, "рисование в консоли")

Circle, Rectangle, Triangle

фигуры реализовывают интерфейс Shape
def accept(self, visitor):

интерфейс ShapeVisitor
def visit_circle(self, circle):
def visit_rectangle(self, rectangle):
def visit_triangle(self, triangle):

реализовать два конкретных посетителя
AreaCalculator, ShapePrinter
"""
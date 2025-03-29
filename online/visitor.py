"""
позволяет добавлять новое поведение
"""
"""
выносит обработку объектов в отдельный класс - посетитель
новое добавить отдельным классом
объекты принимают посетителя и передают ему управление
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
        visitor.visit_text(self)


class Image(Element):
    def __init__(self, file_name):
        self.file_name = file_name

    def accept(self, visitor):
        visitor.visit_image(self)

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
JSONExporter

{"type": "text", "content": "привет мир"}
{"type": "image", "content": "cat.jpg"}
"""
import json

class JSONExporter(Visitor):
    def visit_text(self, text):
        return json.dumps({"type": "text", "content": text.content}, ensure_ascii=False)

    def visit_image(self, image):
        return json.dumps({"type": "image", "content": image.file_name}, ensure_ascii=False)

json_exporter = JSONExporter()
for elem in elements:
    print(elem.accept(json_exporter))
"""
Factory method - создает один объект
Abstract factory - создает набор взаимосвязанных объектов в одном стиле

структура:
абстрактная фабрика - интерфейс/ABC cls, набор методов для создания объектов
конкретные фабрики - реализуют абстрактную фабрику
абстрактные продукты - интерфейс/ABC cls, определяют общее поведение объектов
конкретные продукты - реализуют абстрактные продукты
клиентский код - использует фабрику, работает с интерфейсами

(+)
гарантия совместимости
OCP
изоляция создания объектов
тестирование

применяем когда:
независимость от способа создания компономки и представления продуктов
много семейств объектов
нужна совместная работа объектов из одного семейства

(-)
усложнение структуры
трудно добавить новые продукты
"""

"""#абстрактная фабрика
from abc import ABC, abstractmethod

class GUTFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

#конкретные фабрики
class WindowFactory(GUTFactory):
    def create_button(self):
        return WindowButton()

    def create_checkbox(self):
        return WindowCheckbox()

class MacOSFactory(GUTFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSChecbox()

#абстрактные продукты

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

#конкретные продукты

class WindowButton(Button):
    def render(self):
        return "отрисовка Button в win"

class WindowCheckbox(Checkbox):
    def render(self):
        return "отрисовка Checkbox в win"

class MacOSButton(Button):
    def render(self):
        return "отрисовка Button в MacOS"

class MacOSChecbox(Checkbox):
    def render(self):
        return "отрисовка Checkbox в MacOS"

#клиентский код

def create_ui(factory: GUTFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.render())
    print(checkbox.render())

os_type = "Windows"

if os_type == "Windows":
    factory = WindowFactory()
else:
    factory = MacOSFactory()"""

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowButton(Button):
    def render(self):
        print("Отрисовка кнопки в стиле Windows")

class MacButton(Button):
    def render(self):
        print("Отрисовка кнопки в стиле MacOS")

class WindowCheckbox(CheckBox):
    def render(self):
        print("Отрисовка чекбокса в стиле Windows")

class MacCheckbox(CheckBox):
    def render(self):
        print("Отрисовка чекбокса в стиле MacOS")

class GUTFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass

class WindowsFactory(GUTFactory):
    def create_button(self) -> Button:
        return WindowButton()

    def create_checkbox(self) -> CheckBox:
        return WindowCheckbox()

class MacFactory(GUTFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckbox()


def render_ui(factory: GUTFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

factory = WindowsFactory()
render_ui(factory)

factory = MacFactory()
render_ui(factory)


"""
Abstract factory
система создания комлектов образовательных материалов
модуль генерирует учебные комплекты для направлений:
программирование
история

в комплект входят:
Course - текст темы
Test - набор вопросов
Assignment - задание

3 интерфейса/аbc класса
Course get_content()
Test get_questions()
Assignment get_task()

LearningMaterialFactory абстрактная фабрика: создаёт комплекты материалов
    create_course() -> Course
    create_test() -> Test
    create_assignment() -> Assignment

две конкретные фабрики
ProgrammingMaterialFactory
HistoryMaterialFactory

клиентская функция принимает фабрику и создаёт комплекты материалов курс тест задание
"""
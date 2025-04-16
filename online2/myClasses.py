"""
экземпляр класса - объект построенный по шаблону классу
атрибуты (свойства/поля/переменные) - данные в классе
    атрибуты класса - общие для всех объектов
    атрибуты экземпляра класса - принадлежат конкретному объекту
методы - функции в классе
    обычные - say_hello - метод экземпляра класса
    классовые - @classmethod - получают cls первым аргументов, сам класс, а не объект
    статические @staticmethod - не получает ни self ни cls, просто функции внутри класса
магические методы () - переопределяют стандартное поведение
наследование
    super() - функция, вызывать методы родителя
    mro - method resolution order - порядок разрешения методов
    isinstance() - проверяет, является ли объект экземпляром класса или его потомка
    issubclass() - проверяет, является ли один класс подклассом другого
    object - корневой класс

mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
абстрактный класс - шаблон - базовый класс - интерфейс (в питоне интерфейсом
является абстрактный класс без реализации), нельзя создать экземпляр, содержит абстрактные методы

    абстрактные методы - методы без реализации @abstactmethod
pass - подразумевает что далее что-то может быть добавлено
... - не подразумевает что далее что-то может быть добавлено
композиция - один класс содержит экземпляр другого, а не наследует его
"""
import math


class MyClass:
    pass

#класс/шаблон
class Person:
    #атрибуты класса
    isHuman = True

    def __init__(self, name, age, high=None):
        #атрибуты экземпляра класса
        self.name = name
        self.age = age
        self.high = high

    def say_hello(self):
        print(f"привет я {self.name} мне {self.age}")

    def birthDay(self):
        self.age += 1

    #плохо
    @staticmethod
    def unHuman():
        Person.isHuman = False

    @classmethod
    def toHuman(cls):
        cls.isHuman = True

#p1 - экземпляр класс
p1 = Person("иван", 20)
#атрибуты (свойства/поля/переменные) - данные в классе
"""
p1
name = "иван"
age = 20
"""

p1.say_hello()
print(p1.age)
p1.birthDay()
print(p1.age)
p1.age = 10
print(p1.age)

print(p1.high)
p1.high = 200
print(p1.high)


print(Person.isHuman)
Person.unHuman()
print(Person.isHuman)

#наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def move(self):
        print(f"{self.name} двигается")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        self.age = age
        super().__init__(name)

    def bark(self):
        print(f"{self.name} гав")

class BlackDog(Dog):
    def __init__(self, name, age, color='black'):
        self.color = color
        super().__init__(name, age)

blackDog = BlackDog('dog', 1)
print(blackDog.color)

class Flyer:
    def action(self):
        print('летит')

class Swimmer:
    def action(self):
        print('плывет')

class Duck(Flyer, Swimmer):
    def action(self):
        print('утра начинает действие')
        super().action()
        
d = Duck()
d.action()

#mro
print()
print(Duck.__mro__)
print()

a = Duck.__mro__
for i in a:
    print(i.__name__)


class A:
    def do(self):
        print("A")

class B:
    def do(self):
        print("B")

class C(A):
    def do(self):
        print("C")

class D(B, C):
    pass

d = D()
d.do()

print(D.__mro__)
"""
isinstance() - проверяет, является ли объект экземпляром класса или его потомка
issubclass() - проверяет, является ли один класс подклассом другого"""
"""print(isinstance(d, D))
print(isinstance(d, B))
print(isinstance(d, C))
print(isinstance(d, A))
print(isinstance(d, object))
print(d is D)
print(d is A)
print(d is object)
print(D is D)
print(D is A)"""

"""print(issubclass(D, B))
print(issubclass(D, A))
print(issubclass(B, C))
print(issubclass(D, object))"""
#mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Service(LoggerMixin, object):
    def process(self):
        self.log("обработка данных начата")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

print(bool(Shape.__abstractmethods__))  # проверка на абстрактность

"""
True

False:
""
''
[]
{}
frozenset()
set()
None
0
0.0

if []:
    print(1)
else:
    print(2)

"""

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self) -> float | int:
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area())

s = Square(5)
print(s.area())

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Base(ABC):
    @abstractmethod
    def hello(self):
        print("привет из Base")

class Product(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

class Report(ABC):
    def print_header(self):
        print("отчет")

    @abstractmethod
    def generate(self):
        pass


class Printable:
    def my_print(self):
        print("печатаю")

class Document(ABC, Printable):
    @abstractmethod
    def get_content(self):
        pass

#mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
"""
нет __init__() и отрибутов
предназначен для наследования совместно с другими
заканчивается на Mixin
"""

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Worker:
    def work(self):
        print('работаю')

class LogginWorker(LoggerMixin, Worker):
    pass

lw = LogginWorker()
lw.work()
lw.log('готово')


#композиция - один класс содержит экземпляр другого, а не наследует его

class EngineV6:
    def start(self):
        print('двигатель запущен')

class EngineV4:
    def start(self):
        print('двигатель запущен')

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("машина едет")



class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")

class C(A):
    def do(self):
        print("C")

class D(B, C):
    pass

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def move(self):
        print(f"{self.name} двигается")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        self.age = age
        super().__init__(name)

    def bark(self):
        print(f"{self.name} гав")

    def move(self):
        #хорошо
        super().move()

        #плохо
        Animal.speak(self)

        print()

#super(CurrentClass, self)

class Parent:
    def greet(self):
        print('hi от родителя')

class Child(Parent):
    def greet(self):
        super(Child, self).greet()
        print("hi от ребенка")
        
class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")
        super().do()

class C(A):
    def do(self):
        print("C")
        super().do()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()

#super(ClassName, instance).method()
"""
класс - шаблон, по которому создаются объекты
экземпляр класса - объект построенный по шаблону классу
атрибуты (свойства/поля/переменные) - данные в классе
    атрибуты класса - общие для всех объектов
    атрибуты экземпляра класса - принадлежат конкретному объекту
методы - функции в классе
    обычные - say_hello - метод экземпляра класса
    классовые - @classmethod - получают cls первым аргументов, сам класс а не объект
    статические @staticmethod - не получает ни self ни cls, просто функции внутри класса
магические методы () - переопределяют стандартное поведение
"""
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
    def __init__(self, name, age):
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

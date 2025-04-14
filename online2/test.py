"""
Создать базовыйкласс«Домашнееживотное»ипро
изводныеклассы«Собака»,«Кошка»,«Попугай»,«Хомяк».
Спомощью конструктора установить имя каждого жи
вотного и его характеристики. Реализуйте для каждого
из классов методы:
■ Sound — издает звук животного (пишем текстом в
консоль);
 ■ Show — отображает имя животного;
 ■ Type — отображает название его подвида;
"""

class Pet:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def sound(self):
        print('издает звук')

    def show(self):
        print(f"имя {self.name}")

    def type(self):
        print("Домашнее животное")

class Dog(Pet):
    def sound(self):
        print("гав")

    def type(self):
        print('собака')

class Cat(Pet):
    def sound(self):
        print('мяу')

    def type(self):
        print("кошка")

class Parrot(Pet):
    def sound(self):
        print('чирик')

    def type(self):
        print("попугай")

class Hamster(Pet):
    def sound(self):
        print('хомяк')

    def type(self):
        print("хомяк")


dog = Dog("шарик", "овчарка")
cat = Cat("мурка", "сиамская")

for pet in [dog, cat]:
    pet.show()
    pet.type()
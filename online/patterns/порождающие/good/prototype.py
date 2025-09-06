"""
вместо создания нового объекта с нуля - клонировать уже существующий

используем когда
создание объекта - дорогостояще
объектов много и почти одинаковы
нужны опеделенно инициализированные копии объектов
нужно клонировать во время выполнения программы

import copy
copy.copy(obj) - поверхностная
copy.deepcopy(obj) - глубокая копия

структура:
Prototype - интерфейс для клонирования объекта clone()
ConcretePrototype 
Client - использует clone


прототип - интерфейс с clone()
конкретные прототипы - реализуют clone()
клиент - использует clone()


поверхностное shallow copy()
глубокое копирование deep copy deepcopy()


(+)
быстрое копирование
гибкость
изоляция логики создания
меньше зависимостей

(-)
сложность с глубоким копированием
поддержка в изменениях
может нарушить инкапсуляцию

когда используем:
сложно создать, но часто повторяется с некоторыми изменениями
история
клиент не зависит от конкретных классов продукта
избегать дублирования создания сложных конфигураций


"""

# поверхностная копия
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)
b[2].append(5)
print(a)

# глубокая копия
c = copy.deepcopy(a)
c[2].append(99)
print(a)
print(c)
print(a)

#import copy

class Character:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} {self.weapon} {self.armor}"

original = Character("Hero", "Sword", "Shield")
print(original)

clone1 = original.clone()
clone1.name = "Clone 1"
clone1.weapon = "Bow"

clone2 = original.clone()
clone2.name = "Clone 2"
clone2.armor = "Helmet"

print(clone1)
print(clone2)

print(original)


# import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Car(Prototype):
    def __init__(self, model, color, options):
        self.model = model
        self.color = color
        self.options = options

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Car(model={self.model}, color={self.color}, options={self.options})"

"""if __name__ == "__main__":
    car1 = Car("model", 'color', ['автопилот', "панорамная крыша"])
    print("оригинал", car1)

    car2 = car1.clone()
    car2.color = 'синий'
    car2.options.append("спортивный режим")

    print("копия", car2)
    print("оригинал после клонирования", car1)"""


class Inventory:
    def __init__(self, items):
        self.items = items

class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def clone(self):
        return copy.deepcopy(self)

inv = Inventory(["монета", "ключи", "коробка"])
p1 = Player("Alice", inv)

p2 = p1.clone()
p2.name = "Bob"
p2.inventory.items.append("карта")

print(p1.inventory.items)
print(p2.inventory.items)
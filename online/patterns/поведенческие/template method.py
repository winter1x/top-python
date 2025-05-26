"""
определяет общий алгоритм
изменение отдельных шагов
"""
"""
структура:
basic базовый класс, с prepare()
в prepare() другие методы с возможностью переопределения
concrete подклассы переопределяют только нужное
"""
"""class Tea:
    def prepare(self):
        print("кипятим")
        print("чай")
        print("сахар")
        print("в кружку")

class Coffee:
    def prepare(self):
        print("кипятим")
        print("кофе")
        print("молоко")
        print("в кружку")
        
tea = Tea()
tea.prepare()

coffee = Coffee()
coffee.prepare()"""

from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.add_condiments()
        self.pour()

    def boil_water(self):
        print("кипятим")

    def pour(self):
        print("в кружку")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print("чай")

    def add_condiments(self):
        print("сахар")

class Coffee(Beverage):
    def brew(self):
        print("кофе")

    def add_condiments(self):
        print("молоко")

tea = Tea()
tea.prepare()

print('---------')

coffee = Coffee()
coffee.prepare()
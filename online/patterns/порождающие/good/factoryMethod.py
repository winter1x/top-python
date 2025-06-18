"""
factoryMethod
инкапсулирует процесс создания объекта в отдельных подклассах

струтура:
Product подукт- абстрактный класс, создаваемый объекта
ConcreteProduct конкретный продукт- классы которые наследуются от Product
Creator создатель - абстрактный класс, создает объект с помощью метода factoryMethod
ConcreteCreator конкретный создатель - классы которые наследуются от Creator. Создает конкретный продукт

+
ocp
упрощает тестирование
инкапсуляция создания объекта

-
много классов
повышение абстракции

simple factory просто функция
Abstract Factory создает несколько продуктов, определяя семейство продуктов
"""

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print('Доставлено грузовиком')

class Ship(Transport):
    def deliver(self):
        print('Доставлено кораблем')

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

def client_code(logistics: Logistics):
    logistics.plan_delivery()

client_code(RoadLogistics())
client_code(SeaLogistics())



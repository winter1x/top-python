"""
Strategy
расчет стоимости доставки

обычная доставка с фиксированной ценой
экспресс доставка с ценой выше
самовывоз бесплатный
"""

from abc import ABC, abstractmethod

#интерфейс стратегии
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass

#конкретные стратегии
class StandardDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 200

class ExpressDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 200 + weight * 50

class Pickup(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 0

#контекст
class Order:
    def __init__(self, weight: float, delivery_strategy: DeliveryStrategy):
        self.weight = weight
        self.delivery_strategy = delivery_strategy

    def get_delivery_price(self) -> float:
        return self.delivery_strategy.calculate_cost(self.weight)

order1 = Order(2, StandardDelivery())
order2 = Order(2, ExpressDelivery())
order3 = Order(2, Pickup())

print(order1.get_delivery_price())
print(order2.get_delivery_price())
print(order3.get_delivery_price())